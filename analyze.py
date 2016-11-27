import getTextMetadata
import cleanTaggedData


def analyze(_dir = './data_tagged/'):
    text_md = getTextMetadata.main()
    df_tg, df_tg_md = cleanTaggedData.get_tagged_texts(_dir)
    df_ng = cleanTaggedData.get_ngrams(_dir)

    return text_md, df_tg, df_tg_md, df_ng



if __name__ == "__main__":
    analyze()
