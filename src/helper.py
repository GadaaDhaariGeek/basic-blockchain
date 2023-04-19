import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prepare_data_n(file_path):
    """Fucntion to load the proposer count for each round and for each n.

    Args:
        file_path (str): file path

    Returns:
        dataframe: dataframe having the average number of proposer for each value of n
    """
    bp_df = pd.read_csv(file_path)
    tmp_df = bp_df.groupby(["n", "round"]).agg(count=pd.NamedAgg(column="process", aggfunc="count")).reset_index()
    tmp_df2 = tmp_df.groupby(by=["n"]).agg(avg_propose_count=pd.NamedAgg(column="count", aggfunc="mean")).reset_index()
    tmp_df2["percent_proposers"] = (tmp_df2["avg_propose_count"] / tmp_df2["n"])*100
    return tmp_df2

def prepare_data_k(file_path):
    """Fucntion to load the proposer count for each round and for each k.

    Args:
        file_path (str): file path

    Returns:
        dataframe: dataframe having the average number of proposer for each value of k
    """
    bp_df = pd.read_csv(file_path)
    tmp_df = bp_df.groupby(["k", "n", "round"]).agg(count=pd.NamedAgg(column="process", aggfunc="count")).reset_index()
    tmp_df2 = tmp_df.groupby(by=["k", "n"]).agg(avg_propose_count=pd.NamedAgg(column="count", aggfunc="mean")).reset_index()
    tmp_df2["percent_proposers"] = (tmp_df2["avg_propose_count"] / tmp_df2["n"])*100
    return tmp_df2


def create_plots_n(tmp_df2):
    """Function to create plots for average number of proposers for each value of n

    Args:
        tmp_df2 (dataframe): dataframe havign the data to be plotted
    """
    plt.style.use("ggplot")
    plt.subplots(1, 2, figsize=(18, 6))
    plt.subplot(1, 2, 1)
    sns.pointplot(x=tmp_df2["n"].values, y=tmp_df2["avg_propose_count"].values, color="r", label="avg-proposers-count")
    sns.pointplot(x=tmp_df2["n"].values, y=tmp_df2.n.values, markers="o", color="g", label="y=x line")
    plt.legend()
    plt.title("Impact of # nodes on # block proposers")
    plt.xlabel("Number of nodes in the network")
    plt.ylabel("Avg. number of proposers")
    # plt.show()

    plt.subplot(1, 2, 2)
    sns.pointplot(x=tmp_df2["n"].values, y=tmp_df2["percent_proposers"].values, color="r", label="avg-proposers-percent")
    # sns.pointplot(x=tmp_df2["n"].values, y=tmp_df2.n.values, markers="^", color="g", label="y=x line")
    plt.legend()
    plt.title("Percentage of block proposers as compared to number of nodes")
    plt.xlabel("Number of nodes in the network")
    plt.ylabel("Avg. percentage of proposers")
    plt.yticks(ticks=np.arange(30, 101, 10))
    plt.show()

def create_plots_k(tmp_df2):
    """Function to create plots for average number of proposers for each value of k

    Args:
        tmp_df2 (dataframe): dataframe havign the data to be plotted
    """
    plt.style.use("ggplot")
    plt.figure(figsize=(8, 4))
    # plt.subplots(1, 2, figsize=(18, 4))
    # plt.subplot(1, 2, 1)
    sns.pointplot(x=tmp_df2["k"].values, y=tmp_df2["avg_propose_count"].values, color="r", label="avg-proposers-count")
    # sns.pointplot(x=tmp_df2["k"].values, y=tmp_df2.k.values, markers="o", color="g", label="y=x line")
    plt.legend()
    plt.title("Impact of 'k' (difficulty) on # block proposers")
    plt.xlabel("Difficulty parameter k. d = 2^k")
    plt.ylabel("Avg. number of proposer nodes")
    plt.show()

    # plt.subplot(1, 2, 2)
    # sns.pointplot(x=tmp_df2["k"].values, y=tmp_df2["percent_proposers"].values, color="r", label="avg-proposers-percent")
    # # sns.pointplot(x=tmp_df2["n"].values, y=tmp_df2.n.values, markers="^", color="g", label="y=x line")
    # plt.legend()
    # plt.xlabel("Number of nodes in the network")
    # plt.ylabel("Avg. percentage of proposer nodes")
    # # plt.yticks(ticks=np.arange(0, 101, 10))
    # plt.show()



