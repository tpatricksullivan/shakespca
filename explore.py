import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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


def plot_PCA(Y, md_, title_, p, fig_):

    fig_.add_subplot(1, 2, p)
    for lab, col in zip(md_['First_Folio_category'].unique(),
                        ('blue', 'red', 'green', 'orange')):
        txts = md_['First_Folio_category'] == lab
        plt.scatter(Y.loc[txts, 0], Y.loc[txts, 1], label=lab, c=col, alpha=0.4, s=70)
    for pl in Y.index:
        plt.text(Y.loc[pl, 0]+0.1, Y.loc[pl, 1]+0.1, pl, fontsize=18)
    plt.xlabel('Principal Component 1', fontsize=14)
    plt.ylabel('Principal Component 2', fontsize=14)
    plt.title(title_, fontsize=20)

    return 0
