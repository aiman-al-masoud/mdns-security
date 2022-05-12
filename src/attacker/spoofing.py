def with_linux_spoofing(fn):

    def wrapper(*args, **kwargs):
        #	os.system(f"sudo iptables -t nat -A POSTROUTING -j SNAT --to-source {args.spoofed_ip}")
        print("Spoofing")
        fn(*args, **kwargs)
        print("Despoofing")
        #	os.system(f"sudo iptables -t nat -D POSTROUTING -j SNAT --to-source {args.spoofed_ip}")
    
    return wrapper
    




# @with_linux_spoofing
# def crap(a):
#     print("ciao", a)

# crap("coao")



