import pandas as pd
import getPlayMetadata
import cleanTaggedData
import pandasql

playMd = getPlayMetadata.main()
df, df_md = cleanTaggedData.get_tagged_data("./data_tagged/")



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



