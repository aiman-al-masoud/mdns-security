import sys
import argparse
import dns.resolver
import time

def send_query(host, RRtype):
	Res=dns.resolver.Resolver()
	Res.nameservers=['224.0.0.251'] #mdns multicast address
	Res.port=5353 #mdns port

	try:
		a=Res.resolve(host,RRtype)
		return a[0].to_text()
	except Exception as e:
		pass

def __main__():

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", "-t", help="Set the .local target (necessary)")
    parser.add_argument("--type", "-k", help="Set the RR type to query (necessary)")
    parser.add_argument("--iterations", "-n", help="Set the number of iterations (default 1).")
    args = parser.parse_args()

    niterations = int(args.iterations or "1")

    if len(sys.argv) < 5:
        parser.print_help(sys.stderr)
        sys.exit(1)

    for i in range(niterations):
        start_time=time.time()
        query_result = send_query(args.target,args.type)
        end_time=time.time()-start_time
        print(f"ANSWER: {query_result} (received in {round(end_time,3)} seconds)")

if __name__ == "__main__":
    __main__()