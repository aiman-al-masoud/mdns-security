#!/bin/python3

import signal
import sys
import argparse
import time
import binascii
import socket
sys.path.append("../src/")
from scripton import build_message, signal_handler

multicast_add = "224.0.0.251"
mdns_port = 5353
rr_dict = {"A": 1,"AAAA":28,"TXT":16,"PTR":12,"SRV":33,"ANY":255}

def __main__():
	signal.signal(signal.SIGINT, signal_handler) #CTRL+C to end gracefully
	
	# command line args
	parser = argparse.ArgumentParser()
	parser.add_argument("--target", "-t", help="Set the .local target (necessary).")
	parser.add_argument("--type", "-rr", help="Set the RR type to query (default type A).")
	args = parser.parse_args()

	target =  args.target
	rr = args.type or "A"  # default to type A RR 

	# error out if no target ip provided
	if target is None:
		parser.print_help(sys.stderr)
		sys.exit(1)
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.settimeout(4)

	if rr in rr_dict.keys():
		rr_type = "{:04x}".format(rr_dict[rr])
	else:
		print("Unsupported RR type\n")
		sys.exit(1)
	
	try:
		i=0
		while True:
			try:
				query_time = time.time()
				message = build_message(rr_type, target)
				message = message.replace(" ", "").replace("\n", "") 
				sock.sendto(binascii.unhexlify(message), (multicast_add, mdns_port))
				data, _ = sock.recvfrom(4096)
				print("ID: "+ str(i) +" - time: "+str(round(1000*(time.time()-query_time),3))+" ms")
				i += 1;
				time.sleep(0.5)
			except socket.timeout as e:
				print(e)
	except SystemExit as e:
		sock.close()
		print("Good bye!\n")

	
if __name__ == "__main__":
	__main__()
