import pandas as pd
import createPlayMap
import cleanTaggedData


def analyze(_dir):
    playmap = createPlayMap.main()
    df, df_metadata = cleanTaggedData.get_tagged_data(_dir)
    print df.info()
    print df.metadata.info()
    return 0

if __name__ == "__main__":
    analyze('./data_tagged/')
