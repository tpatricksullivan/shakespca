import os
import pandas as pd


def main(input_file = 'playMetadata.csv'):

    playmap = pd.read_csv(input_file)
    # playmap['play_code'] = playmap['play_code'].apply(lambda x: x.lower())
    assert isinstance(playmap, pd.DataFrame)

    return playmap


if __name__ == "__main__":
    main('playMetadata.csv')
