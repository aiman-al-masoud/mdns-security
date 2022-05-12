from dns.resolver import Resolver
from dns.resolver import LifetimeTimeout
import logging


def send_query(host, rr_type) -> None:
        
        r = Resolver()
        r.nameservers = ['224.0.0.251'] #mdns multicast address
        r.port = 5353 #mdns port

        try:
            a = r.resolve(host, rr_type)
            logging.info("response")
        except LifetimeTimeout as lft_exp:  
            logging.info("timeout")


# send_query("1.1.1.1", "A")