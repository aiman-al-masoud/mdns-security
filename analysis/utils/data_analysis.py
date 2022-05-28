import os, pandas as pd, numpy as np
from matplotlib import pyplot as plt
from analysis_utils import *
from scipy.stats import mannwhitneyu


def read_file(filename):
    with open(filename) as f:
        return f.read()


def plot_RTT_per_ping(filename):
    dump = read_file(filename)
    s = pd.Series(dump_to_rtt_list(dump))
    s = s.apply(lambda x : float(x) if isinstance(x, float) else  np.inf)
    fig, ax = plt.subplots(figsize=(8,3))
    ax.set_xlabel("Ping number")
    ax.set_ylabel("RTT (ms)")
    ax.set_title("RTTs for each ping request".title())
    plt.figtext(1.33, 0.65, get_description(dump), wrap=True, horizontalalignment='center', fontsize=12)
    s.plot(ax=ax, color='b')


def set_bp_color_properties(boxplot):
    for _, line_list in boxplot.items():
        for line in line_list:
            line.set_color('b')
    for median in boxplot['medians']:
        median.set(color='#90EE90', linewidth=1.5)


""" Boxplot of only when system was under attack and when not """
def plot_boxplot1(path, return_my_dict = False):
    my_dict = {}
    my_dict["No attack"] = []
    my_dict["Attack"] = []
    for i, filename in enumerate(os.listdir(path)):
        s = dump_to_rtt_list(read_file(path + filename))
        first_in_first = find_timeout_indexes(s)[0]
        one_last_thing = find_timeout_indexes(s)[-1]    
        attack_rtts = s[first_in_first:one_last_thing+1]
        no_attack_rtts = s[-(one_last_thing+1):first_in_first]
        my_dict["No attack"].extend(no_attack_rtts)
        my_dict["Attack"].extend(attack_rtts)
    fig, ax = plt.subplots()
    ax.set_ylabel("RTTs (ms)")
    ax.set_title('Ping RTTs - Network under attack & not')
    bp = ax.boxplot(my_dict.values(), showmeans=True, meanprops={"marker":"s","markerfacecolor":"#90EE90", "markeredgecolor":"green"})
    ax.set_xticklabels(my_dict.keys())
    set_bp_color_properties(bp)
    if (return_my_dict):
        return my_dict


def get_attacks_description():
    return "Attack 1__ 1 attacker, 1 thread, rr:ANY, pinged device:target\nAttack 2__ 1 attacker, 100 threads, rr:ANY, pinged device:target\nAttack 3__ 1 attacker, 300 threads, rr:PTR, pinged device:target\nAttack 4__ 1 attacker, 300 threads, rr:A, pinged device:target\nAttack 5__ 1 attacker, 300 threads, rr:ANY, pinged device:target\nAttack 6__ 1 attacker, 10 threads, rr:ANY, pinged device:target\nAttack 7__ 2 attackers, 300 threads, rr:ANY, pinged device:target\nAttack 8__ 2 attackers, 300 threads, rr:ANY, pinged device:another node\n"


""" Boxplot of different attacks """
def plot_boxplot2(path):
    i = 0
    my_dict = {}
    for i, filename in enumerate(os.listdir(path)):
        i += 1
        s = dump_to_rtt_list(read_file(path + filename))
        first_in_first = find_timeout_indexes(s)[0]
        one_last_thing = find_timeout_indexes(s)[-1]    
        attack_rtts = s[first_in_first:one_last_thing+1]
        my_dict[str(i)] = attack_rtts
    my_dict = dict(sorted(my_dict.items()))
    fig, ax = plt.subplots()
    ax.set_xlabel("Attack ID")
    ax.set_ylabel("RTTs (ms)")
    ax.set_title('Ping RTTs - Network under attack\n(different attacks)')
    bp = ax.boxplot(my_dict.values(), showmeans=True)
    plt.figtext(1.5, 0.3, get_attacks_description(), wrap=True, horizontalalignment='center', fontsize=12)
    set_bp_color_properties(bp)


def perform_mannwhitneyu_test(path, alpha):
    my_dict = plot_boxplot1(path, True)
    res = mannwhitneyu(my_dict["No attack"], my_dict["Attack"])
    if (res[1] < alpha):
        statistical_significant = "Yes :)  - different means"
    else: statistical_significant = "No :'(  - random sampling"
    print("Mann-Whitney U test(statistics: " + str(res[0]) + ", p-value: " + str(res[1]) + ")\nStatistical significant? " + statistical_significant)
