import re
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from analysis_utils import *
import os

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

def find_timeout_indexes(s):
    timeout_index_list = []
    for i in range(len(s)):
        if s[i] == 4000:
            timeout_index_list.append(i)
    return timeout_index_list

def plot_boxplot(path):
    my_dict = {}
    i = 0
    for filename in os.listdir(path):
        i += 1
        s = pd.Series(dump_to_rtt_list(read_file(path + filename)))
        first_in_first = find_timeout_indexes(s)[0]
        one_last_thing = find_timeout_indexes(s)[-1]
        attack_rtts = s[first_in_first:one_last_thing+1]
        if i == 1:
            my_dict["No attack"] = s[-(one_last_thing+1):first_in_first]
        my_dict["Attack_"+str(i)] = attack_rtts
    fig, ax = plt.subplots()
    ax.set_title('Box Plot, average RTTs')
    ax.boxplot(my_dict.values(), showmeans=True)
    ax.set_xticklabels(my_dict.keys(), rotation=90)