import pandas as pd
import getTextMetadata
import cleanTaggedData
import pandasql
import numpy as np
import analyze
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA as sklearnPCA


text_md, df_tg, df_tg_md, df_ng = analyze.analyze()
sklearn_pca = sklearnPCA(n_components = 2)
df_justS = df_tg.index.isin(['prideandprejudice','leviathan'])
df_transform = sklearn_pca.fit_transform(df_tg[~df_justS])

with plt.style.context('fivethirtyeight'):
    plt.figure(figsize=(6, 4))
    for lab, col in zip(('History', 'Comedy', 'Tragedy'),
                        ('blue', 'red', 'green')):
        pls = text_md.First_Folio_category[ text_md['First_Folio_category']==lab].index
        df_tg[~df_justS]
        plt.scatter(df_transform[pls, 0],
                    df_transform[pls, 1],
                    label=lab,
                    c=col)
    #for i in range(0,39):
    #    plt.text( df_transform[i,0], df_transform[i,1], df_md.text_key[i])
    #plt.text( df_transform[:,0], df_transform[:,1], df_tg.index)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()



## Plot histogram of each variable

## http://www.gutenberg.org/cache/epub/1041/pg1041.txt





# with matplotlib.pyplot.style.context('fivethirtyeight'):
#     matplotlib.pyplot.figure(figsize=(6, 4))
#     for lab, col in zip(('History', 'Comedy', 'Tragedy'),
#                         ('blue', 'red', 'green')):
#         pls = df_md_cat.First_Folio_category[ df_md_cat['First_Folio_category']==lab].index
#         matplotlib.pyplot.scatter(Y_sklearn[pls, 0],
#                     Y_sklearn[pls, 1],
#                     label=lab,
#                     c=col)
#     for i in range(0,39):
#         matplotlib.pyplot.text( Y_sklearn[i,0], Y_sklearn[i,1], df_md_cat.text_key[i])
#     matplotlib.pyplot.text( 1,1, 'hello' )
#     matplotlib.pyplot.xlabel('Principal Component 1')
#     matplotlib.pyplot.ylabel('Principal Component 2')
#     matplotlib.pyplot.legend(loc='lower left')
#     matplotlib.pyplot.tight_layout()
#     matplotlib.pyplot.show()
#
# sklearn = sklearnPCA(n_components = 3)
# Y_sklearn = sklearn.fit_transform(df)
# # from mpl_toolkits.mplot3d import Axes3D
#
# with matplotlib.pyplot.style.context('fivethirtyeight'):
#     fig = matplotlib.pyplot.figure(figsize=(6, 4))
#     fig.add_
#     for lab, col in zip(('History', 'Comedy', 'Tragedy'),
#                         ('blue', 'red', 'green')):
#         pls = df_md_cat.First_Folio_category[ df_md_cat['First_Folio_category']==lab].index
#         Axes3D.scatter(Y_sklearn[pls, 0],
#                     Y_sklearn[pls, 1],
#                     Y_sklearn[pls, 2],
#                     label=lab,
#                     c=col)
#     # for i in range(0,39):
#     #     matplotlib.pyplot.text( Y_sklearn[i,0], Y_sklearn[i,1], df_md_cat.text_key[i])
#     # matplotlib.pyplot.text( 1,1, 'hello' )
#     # matplotlib.pyplot.xlabel('Principal Component 1')
#     # matplotlib.pyplot.ylabel('Principal Component 2')
#     # matplotlib.pyplot.legend(loc='lower left')
#     # matplotlib.pyplot.tight_layout()
#     # matplotlib.pyplot.show()
#
#
#
# matplotlib.pyplot.imshow (sklearn_pca.components_)



