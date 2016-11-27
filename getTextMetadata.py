import os
import pandas as pd


def main(input_file = 'textMetadata.csv'):

    text_md = pd.read_csv(input_file)
    text_md['text_code'] = text_md['text_code'].apply(lambda x:x.lower())
    text_md.set_index('text_code', inplace=True)
    assert isinstance(text_md, pd.DataFrame)

    return text_md


if __name__ == "__main__":
    main('textMetadata.csv')
