import os
import re
import pandas as pd
import glob
from datetime import datetime
from collections import defaultdict


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


def get_tagged_texts(_dir = './data_tagged/'):
    """Retun tuple(dataframe of just values, dataframe of metadata)
    """
    latest = find_latest_Ubq(_dir)
    output_file = os.path.join(_dir, latest, 'csv', 'data-ubiq.csv')
    if not os.path.exists(output_file):
        raise IOError("could not find file %s" % output_file)
    df = pd.read_csv(output_file)
    df_metadata = df[list(metadata_columns)]
    df = df[df.columns.difference(metadata_columns)]

    return df, df_metadata


def find_latest_Ubq(_dir = './data_tagged/'):
    """Find the latest set of tagged results
    in a directory of Ubq parsing results."""
    dirs = pd.Series( os.listdir(_dir))
    if len(dirs) == 0:
        raise StandardError("directory %s is empty" % _dir)
    dirs = dirs.apply( lambda x: x.strip('ubq-data-'))
    dirs = dirs.apply( lambda x: datetime.strptime(x, "%Y-%m-%d-%H-%M-%S"))
    latest = dirs.max()
    res = 'ubq-data-%s' % latest.strftime("%Y-%m-%d-%H-%M-%S")

    return res


def get_ngrams(_dir = './data_tagged/'):
    """Get mxn matrix of m texts and n n-gram frequencies"""
    latest = find_latest_Ubq(_dir)
    output_dir = os.path.join(_dir, latest, 'ngram', 'perDocNgrams', 'data*1grams.csv')
    output_files = glob.glob(output_dir)
    res = defaultdict(lambda: defaultdict(lambda: 0))
    for f in output_files:
        m = re.search('/data-(.*)-1grams.csv', f)
        if not m:
            raise IOError("file %s is not a 1gram data file" % f)
        text_key = m.group(1)
        with open(f, 'r') as f_reading:
            f_reading.next()
            for line in f_reading:
                (word, freq, rank) = line.rsplit(',', 2)
                if not bool(re.match("[0-9\.]+", word)):
                    res[text_key][word] = int(freq)
    res = pd.DataFrame.from_dict(res, orient='index')
    res = res.div( res.sum(axis = 1), axis = 0 ) * 100
    return res


if __name__ == "__main__":
    get_tagged_texts()
    get_ngrams()
