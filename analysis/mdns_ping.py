#!/bin/python3

import signal
import os
import sys
import argparse
import time
from scripton import signal_handler

def __main__():
	signal.signal(signal.SIGINT, signal_handler) #CTRL+C to end gracefully
	
	# command line args
	parser = argparse.ArgumentParser()
	parser.add_argument("--target", "-t", help="Set the .local target (necessary).")
	args = parser.parse_args()

	target =  args.target

	# error out if no target ip provided
	if target is None:
		parser.print_help(sys.stderr)
		sys.exit(1)
	
	try:
		while True:
			query_time = time.time()
			os.system(f"avahi-resolve-host-name {target}")
			print("Time: "+str(round((time.time()-query_time)*1000,3))+" ms\n")
			time.sleep(1)
	except Exception as e:
		print(e)
		print("Good bye!\n")

	
if __name__ == "__main__":
	__main__()
