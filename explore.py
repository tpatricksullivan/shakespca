import pandas as pd
import getTextMetadata
import cleanTaggedData
import pandasql
import numpy as np
import analyze
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from collections import namedtuple


def Principal_Components(A):
    assert (isinstance(A, pd.DataFrame))

    # Standardize input by subtracting mean
    A_std = (A - A.mean(axis=0))

    # Calculate covariance matrix (without scaling by number of samples)
    covA = A_std.T.dot(A_std)

    # Calculate eigenvectors and values
    eig_val, eig_vec = np.linalg.eigh(covA)

    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(eig_val[i], eig_vec[:, i]) for i in range(len(eig_val))]

    #  Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    # Return ordered eigenvalue and eigenvectors
    eig_val = [i[0] for i in eig_pairs]
    eig_vec = np.asmatrix([i[1] for i in eig_pairs]).T

    # Return everything in a tuple with named elements
    res = namedtuple("PC_", ['A_std', 'covA', 'eig_val', 'eig_vec'])

    return res(A_std, covA, eig_val, eig_vec)


def PC_Transform(inp, n_components):
    PC_inp = Principal_Components(inp)
    topneigv = PC_inp.eig_vec[:, range(0, n_components)]

    return inp.dot(topneigv)


def plot_PCA(Y, md_):
    # Coerce Y to a data frame if it is a matrix
    Y = pd.DataFrame(Y, index = md.index)

    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(6, 4))
        for lab, col in zip( md_['First_Folio_category'].unique(),
                            ('blue', 'red', 'green', 'orange')):
            txts = md['First_Folio_category'] == lab
            plt.scatter(Y.loc[txts,0], Y.loc[txts,1], label=lab, c=col)
        for pl in Y.index:
            plt.text(Y.loc[pl, 0], Y.loc[pl, 1], pl)
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.legend(loc='lower left')
        plt.tight_layout()
        plt.show()

    return 0


md, A_tg, A_md, A_ng = analyze.analyze()



A_tg, A_md = cleanTaggedData.get_tagged_texts()
md =  getTextMetadata.main()
justPlays = list(md.query('First_Folio_category != "Other"').index)
justShak = list(md.index[md['Shakespeare']])
justPlays_tg = A_tg.loc[ justPlays ]
justShak_tg = A_tg.loc[ justShak ]
A_tg.iloc[:,0:5].head()
A_ng = cleanTaggedData.get_ngrams()
justPlays_ng = A_ng.loc[justPlays]
justShak_ng = A_ng.loc[justShak]
A_ng.iloc[:,0:5].head()

A_ng_pc1 = PC_Transform(A_ng,2)

sklearn_pca = sklearnPCA(n_components = 2, svd_solver = 'full')
A_tg_pc = sklearn_pca.fit_transform(A_tg)
#df_justS = df_tg.index.isin(['prideandprejudice','leviathan'])


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



