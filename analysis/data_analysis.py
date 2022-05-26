import re
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from analysis_utils import *

def read_file(filename):
    with open(filename) as f:
        return f.read()

def plot_RTT_per_ping(filename):
    dump = read_file(filename)
    s = pd.Series(dump_to_rtt_list(dump))
    s = s.apply(lambda x : float(x) if isinstance(x, float) else  np.inf)
    fig, ax = plt.subplots(figsize=(8,3))
    ax.set_xlabel("ping number")
    ax.set_ylabel("RTT (ms)")
    ax.set_title("RTT for each ping req".title())
    s.plot(ax=ax)