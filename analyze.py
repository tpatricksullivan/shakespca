import getPlayMetadata
import cleanTaggedData


def analyze(_dir = './data_tagged/'):
    playmap = getPlayMetadata.main()
    df, df_md = cleanTaggedData.get_tagged_texts(_dir)
    df_ng = cleanTaggedData.get_ngrams(_dir)

    return playmap, df, df_md, df_ng



if __name__ == "__main__":
    analyze()
