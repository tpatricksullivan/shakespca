import os
import pandas as pd
from datetime import *


metadata_columns = {'text_name',
                    'text_key',
                    'token_csv_name',
                    'chunk_index',
                    '!UNRECOGNIZED',
                    '!UNTAGGED',
                    '!BLACKLISTED',
                    '<# Word Tokens>',
                    '<# Punctuation Tokens>',
                    '<# Tokens>'}


def get_tagged_data(_dir):
    """
    :returns tuple(dataframe of just values, dataframe of metadata
    """
    latest = find_latest_Ubq(_dir)
    output_file = os.path.join(_dir, latest, 'csv/data-ubiq.csv')
    if not os.path.exists(output_file):
        raise StandardError("could not find file %s" % output_file)
    df = pd.read_csv(output_file)
    df_metadata = df[list(metadata_columns)]
    df = df[df.columns.difference(metadata_columns)]

    return df, df_metadata


def find_latest_Ubq(_dir):
    """Finds the latest set of tagged results
    in a directory of Ubq parsing results."""
    dirs_df = pd.DataFrame( os.listdir(_dir))
    if len(dirs_df) == 0:
        raise StandardError("directory %s is empty" % _dir)
    dirs_df[0] = dirs_df[0].apply( lambda x: x.strip('ubq-data-'))
    dirs_df[0] = dirs_df[0].apply( lambda x: datetime.strptime(x, "%Y-%m-%d-%H-%M-%S"))
    res = 'ubq-data-%s' % dirs_df[0].sort_values()[0].strftime("%Y-%m-%d-%H-%M-%S")

    return res

if __name__ == "__main__":
    get_tagged_data('./data_tagged/')
