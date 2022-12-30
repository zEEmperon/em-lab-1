import pandas as pd
import numpy as np


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    # loading .csv file
    # filename = "data.csv"
    # df = load_csv(filename)
    Var = 16
    loc = Var
    scale = Var / 10
    size = Var * 10
    a = np.random.normal(loc, scale, size)
    print(a)


if __name__ == '__main__':
    main()
