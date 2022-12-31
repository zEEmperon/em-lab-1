import math
import pandas as pd
import numpy as np
import functools
import matplotlib.pyplot as plt


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    Var = 16
    loc = Var
    scale = Var / 10
    size = Var * 10

    filename = "data.csv"
    df = load_csv(filename)

    # histogram
    plt.hist(df["Data"])
    plt.title("Гістограма")
    # plt.show()

    min = math.floor(df["Data"].min())
    max = math.ceil(df["Data"].max())

    # Frequency table
    print()
    print("Building frequency table")
    print()
    freq_data = df.apply(pd.Series.value_counts, bins=[*range(min, max + 1)])

    print(freq_data)


if __name__ == '__main__':
    main()
