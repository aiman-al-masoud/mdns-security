import threading
from threading import Thread
from send_query import send_query
import logging

class SenderThread(Thread):

    """
    Repeatedly sends queries
    """
    
    def __init__(self, host, rr_type):
        Thread.__init__(self)
        self.host, self.rr_type = host, rr_type
        self.running = False
        self.daemon = True # gets killed as soon as the main thread is
    
    def run(self):

        logging.info(f"{self.getName()} summoned")
        self.running = True

        while self.running:
            send_query(self.host, self.rr_type)

    def stop(self):
        logging.info(f"{self.getName()} killed")
        self.running = False