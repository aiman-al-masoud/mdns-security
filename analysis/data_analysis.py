import re
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from analysis_utils import *


def read_file(filename):
    with open(filename) as f:
        return f.read()

def get_description(dump):
    lines = dump.split("\n")
    l = [l[1:] for l in lines if (l and (l[0] == '#'))]
    return '\n'.join(l)

def plot_RTT_per_ping(filename):
    dump = read_file(filename)
    s = pd.Series(dump_to_rtt_list(dump))
    s = s.apply(lambda x : float(x) if isinstance(x, float) else  np.inf)
    fig, ax = plt.subplots(figsize=(8,3))
    ax.set_xlabel("ping number")
    ax.set_ylabel("RTT (ms)")
    ax.set_title("RTT for each ping req".title())
    plt.figtext(1.33, 0.65, get_description(dump), wrap=True, horizontalalignment='center', fontsize=12)
    s.plot(ax=ax)

def plot_boxplot(path):
    my_dict = {}
    
    for i, filename in enumerate(os.listdir(path)):
        
        s = dump_to_rtt_list(read_file(path + filename))
        
        first_in_first = find_timeout_indexes(s)[0]
        one_last_thing = find_timeout_indexes(s)[-1]    
        
        attack_rtts = s[first_in_first:one_last_thing+1]
        
        if i+1 == 1:
            my_dict["No attack"] = s[-(one_last_thing+1):first_in_first]
            
        my_dict["Attack_"+str(i+1)] = attack_rtts
        
    fig, ax = plt.subplots()
    ax.set_title('Box Plot, average RTTs')
    ax.boxplot(my_dict.values(), showmeans=True)
    ax.set_xticklabels(my_dict.keys(), rotation=90)