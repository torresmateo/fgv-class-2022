import matplotlib as mp
import matplotlib.image as im
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def get_dog_image():
    return rgb2gray(im.imread("images/numpy-tutorial/doggo.jpeg")).astype(int)

def plot_image(a):
    fig, ax = plt.subplots()
    ax.imshow(a, cmap="gray")
    plt.show()
    plt.close("all")
    
def plot_distribution(a, title=""):
    f = sns.displot(x=a)
    f.set_axis_labels("Samples", "Count")
    f.ax.set_title(title)
    plt.show()
    plt.close("all")
    
def plot_graph_links_in_bits(nbits):
    fig, ax = plt.subplots(figsize = (7,7), dpi=100)
    
    x = np.arange(1000000, dtype=np.int64)
    y = (x * (x-1) // 2) * (nbits)
    ax.plot(x, y, label="undirected")
    
    avg_lap = 6.4e+10
    ax.axhline(y=avg_lap, color="green", label="8GB (average laptop)")
    nnodes = np.argmin(np.abs(y - avg_lap))
    ax.axvline(x=nnodes, color="green", ls=":", label=f"{nnodes:,} nodes")
    
    exp_lap = 2.56e+11
    ax.axhline(y=exp_lap, color="orange", label="64GB (expensive personal computer)")
    nnodes = np.argmin(np.abs(y - exp_lap))
    ax.axvline(x=nnodes, color="orange", ls=":", label=f"{nnodes:,} nodes")

    server = 2.4e+12
    ax.axhline(y=server, color="red", label="300GB (dedicated server ~30USD+/day)")
    nnodes = np.argmin(np.abs(y - server))
    ax.axvline(x=nnodes, color="red", ls=":", label=f"{nnodes:,} nodes")
    
    ax.set_xlabel("nodes")
    ax.set_ylabel("bits")

    ax.set_title(f'Memory requirements using {nbits} bits')
    ax.legend()
    
    plt.show()
    plt.close("all")
    
def alpha_range(n):
    return char_range('a', chr(ord('a') + n))
    
def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)):
        yield chr(c)
