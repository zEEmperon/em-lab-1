from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    # loading .csv file
    filename = "data.csv"
    df = load_csv(filename)


if __name__ == '__main__':
    main()
