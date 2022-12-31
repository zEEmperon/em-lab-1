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

    minValue = math.floor(df["Data"].min())
    maxValue = math.ceil(df["Data"].max())

    # Frequency table
    freq_data = df.apply(pd.Series.value_counts, bins=[*range(minValue, maxValue + 1)])

    print()
    print("Building frequency table")
    print()
    print(freq_data)

    # Statistics summary
    a = 1

    print()
    print("Statistics summary")
    print()



if __name__ == '__main__':
    main()
