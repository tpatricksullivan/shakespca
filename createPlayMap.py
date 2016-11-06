import os
import pandas as pd


def main(input_file = 'playmap.csv'):

    playmap = pd.read_csv(input_file)
    assert isinstance(playmap, pd.DataFrame)
    return playmap

if __name__ == "__main__":
    main('playmap.csv')
