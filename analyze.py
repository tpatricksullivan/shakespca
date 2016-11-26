import pandas as pd
import getPlayMetadata
import cleanTaggedData
import pandasql
from sklearn.decomposition import PCA as sklearnPCA


def analyze(_dir = './data_tagged/'):
    playmap = getPlayMetadata.main()
    df, df_md = cleanTaggedData.get_tagged_data(_dir)

    return playmap, df, df_md


if __name__ == "__main__":
    analyze()
