import os
import re
import pandas as pd


def main(input_file):

    playmap = pd.read_csv(input_file)
    playmap['play_code'] = playmap['text_name'].apply(lambda x: re.sub('\.txt', '', x))
    col = ['play_code', 'text_name']
    playmap[col] = playmap[col].applymap(lambda x: x.upper())
    write(playmap, input_file)
    return playmap

def write(input_df, input_file):
    input_df.to_csv( os.path.splitext(input_file)[0] + '_out.csv', )
    return 0

if __name__ == "__main__":
    main('playmap.csv')