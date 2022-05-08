import os
import argparse


class Attacker:

    """
    This attacker is still a stub for now...
    """

    def __init__(self, **kwargs):
        self.params = {"spoofed_ip": "10.20.5.1"}
        self.params.update(kwargs)
        # Set the IP in UDP headers to some arbitrary value `spoofed_ip`.
        os.system(f"sudo iptables -t nat -A POSTROUTING -j SNAT --to-source {self.params['spoofed_ip']}")

    def __del__(self):
        """
        Resets the IP (disables spoofing on system) 
        """
        os.system(
            f"sudo iptables -t nat -D POSTROUTING -j SNAT --to-source {self.params['spoofed_ip']}")

    def send_packet(self, target_ip, target_port, message):
        """
        Sends a (spoofed) udp packet to a target ip (server)
        """
        # os.system(f"echo {message} | nc -u {target_ip} {target_port} &")
        # TODO: do something with avahi?

def __main__():
    """
    Ctrl+C to quit me
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-server", "-s",
                        help="Set the ip of the target server.")
    parser.add_argument("--target-port", "-p",
                        help="Set the ip of the target port on the target server.")
    parser.add_argument("--spoofed-ip", "-i", help="Set the spoofed ip.")
    parser.add_argument("--payload", "-m", help="Set the message's payload")
    args = parser.parse_args()
    Attacker(spoofed_ip=args.spoofed_ip).send_packet(args.target_server, args.target_port, args.payload)


if __name__ == "__main__":
    __main__()
