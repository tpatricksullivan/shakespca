import pandas as pd


def main(input_file = 'textMetadata.csv'):

    text_md = pd.read_csv(input_file)
    text_md['text_index'] = text_md['text_code'].apply(lambda x:x.lower())
    text_md.set_index('text_index', inplace=True)
    text_md.sort_index(axis=0, ascending=True, inplace=True)
    assert isinstance(text_md, pd.DataFrame)

    return text_md


if __name__ == "__main__":
    main('textMetadata.csv')
