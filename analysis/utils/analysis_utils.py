import re

TIMEOUT = 4000

def line_to_rtt(l, mdns=False)-> float:

    """
    Get the RTT from a single line of a ping-dump.
    Returns 'timeout' if it detects a timeout.
    Returns None if the line does not contain an RTT.
    """
    try:
        if not mdns:
            return float(re.findall( "time=\d+.\d+" ,l )[0].replace("time=", ""))
        else:
            return float(re.findall( "time: \d+.\d+" , l)[0].replace("time: ", ""))
    except:
        if "timeout" in l:
            return TIMEOUT
        return None


def dump_to_rtt_list(dump, mdns=False):
    """
    Get a list of rtts from a ping dump. 
    """
    return [line_to_rtt(l, mdns) for l in dump.split("\n")]


def find_timeout_indexes(s):
    return [i for i, t in enumerate(s) if t and (t == TIMEOUT)]

def find_indexes_mdns(indexes):
    valid_timeout = []
    for i in range(len(indexes)-1):
        if indexes[i]+1 == indexes[i+1]:
            valid_timeout.append(indexes[i])
    return valid_timeout

def get_description(dump):
    lines = dump.split("\n")
    l = [l[1:] for l in lines if (l and (l[0] == '#'))]
    return '\n'.join(l)