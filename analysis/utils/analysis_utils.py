import re

TIMEOUT = 4000

def dump_to_stats(dump):
    """
    Get the final rtt stats from a ping dump.
    """
    labels = ["rtt_min", "rtt_avg", "rtt_max", "rtt_mdev"]
    last_line = dump.split("\n")[-2]
    numbers =  [ float(t) for t in re.findall("\d+.\d+",  last_line )  ]
    assert len(labels) == len(numbers) 
    return dict(zip(labels, numbers))


def get_avg_rtt(dump):
        
    """
    Get the average rtt from a ping dump.
    """
    return dump_to_stats(dump)["rtt_avg"]


def line_to_rtt(l)-> float:

    """
    Get the RTT from a single line of a ping-dump.
    Returns 'timeout' if it detects a timeout.
    Returns None if the line does not contain an RTT.
    """
    try:
        return float(re.findall( "time=\d+.\d+" ,l )[0].replace("time=", ""))
    except:
        if "timeout" in l:
            return TIMEOUT
        return None


def dump_to_rtt_list(dump):
    """
    Get a list of rtts from a ping dump. 
    """
    return [line_to_rtt(l) for l in dump.split("\n")]


def find_timeout_indexes(s):
    return [i for i, t in enumerate(s) if t and (t == TIMEOUT)]