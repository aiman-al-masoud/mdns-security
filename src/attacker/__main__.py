from sender_thread import SenderThread
import signal
import sys
import argparse
from time import sleep
import logging
logging.basicConfig(filename='app.log', filemode='w+', format='%(asctime)s %(funcName)s(): %(message)s', level= logging.INFO )


def __main__():

	def signal_handler(sig, frame):
		
		for t in threads:
			t.stop()
		
		sys.exit(0)

	signal.signal(signal.SIGINT, signal_handler) #CTRL+C to end gracefully
    
	# command line args
	parser = argparse.ArgumentParser()
	parser.add_argument("--target", "-t", help="Set the .local target (necessary).")
	parser.add_argument("--type", "-k", help="Set the RR type to query (default type A).")
	parser.add_argument("--spoofed-ip", "-i", help="Set the spoofed ip default no spoofing).")
	parser.add_argument("--parallelism", "-p", help="Set the number of sender threads (default 1 thread).")
	args = parser.parse_args()

	target =  args.target
	rr_type = args.type or "A" # default to type A RR 
	# spoofed_ip = # default to NO spoofing
	parallelism = int(args.parallelism or "1") # default to NO parallelism

	# error out if no target ip provided
	if target is None:
		parser.print_help(sys.stderr)
		sys.exit(1)

	# create n threads
	logging.info(f"summoning {parallelism} threads")
	threads = [ SenderThread(args.target, rr_type) for i in range(parallelism)]

	# start them
	for t in threads:
		t.start()	
	
	# main thread waits
	while True:
		pass


if __name__ == "__main__":
    __main__()
	
