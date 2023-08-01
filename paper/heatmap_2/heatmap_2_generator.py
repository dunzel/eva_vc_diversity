import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl


def get_heatmap():
    mpl.rcParams['font.size'] = 16

    data = pd.read_csv('../table_3/table_2_results.csv')

    uniform1_data = data[data['distribution'] == 'uniform1']

    gen_pivot_n_mu = uniform1_data.pivot_table(index='n', columns='mu', values='gen', aggfunc='mean')
    gen_pivot_n_alpha = uniform1_data.pivot_table(index='n', columns='alpha', values='gen', aggfunc='mean')
    gen_pivot_mu_alpha = uniform1_data.pivot_table(index='mu', columns='alpha', values='gen', aggfunc='mean')

    d_rho_pivot_n_mu = uniform1_data.pivot_table(index='n', columns='mu', values='d_rho', aggfunc='mean')
    d_rho_pivot_n_alpha = uniform1_data.pivot_table(index='n', columns='alpha', values='d_rho', aggfunc='mean')
    d_rho_pivot_mu_alpha = uniform1_data.pivot_table(index='mu', columns='alpha', values='d_rho', aggfunc='mean')

    best_rho_pivot_n_mu = uniform1_data.pivot_table(index='n', columns='mu', values='best_rho', aggfunc='mean')
    best_rho_pivot_n_alpha = uniform1_data.pivot_table(index='n', columns='alpha', values='best_rho', aggfunc='mean')
    best_rho_pivot_mu_alpha = uniform1_data.pivot_table(index='mu', columns='alpha', values='best_rho', aggfunc='mean')

    fig, axes = plt.subplots(3, 3, figsize=(15, 15))

    # Create the heatmaps for 'gen'
    sns.heatmap(gen_pivot_n_mu, cmap='binary', annot=True, fmt=".0f", cbar=False, ax=axes[0][0])
    axes[0][0].set_title('n and μ')
    axes[0][0].set_xlabel('')
    axes[0][0].set_ylabel('')

    sns.heatmap(gen_pivot_n_alpha, cmap='binary', annot=True, fmt=".0f", cbar=False, ax=axes[0][1])
    axes[0][1].set_title('n and α')
    axes[0][1].set_xlabel('')
    axes[0][1].set_ylabel('')

    sns.heatmap(gen_pivot_mu_alpha, cmap='binary', annot=True, fmt=".0f", cbar=False, ax=axes[0][2])
    axes[0][2].set_title('μ and α')
    axes[0][2].set_xlabel('')
    axes[0][2].set_ylabel('')

    # Create the heatmaps for 'd_rho'
    sns.heatmap(d_rho_pivot_n_mu, cmap='binary', annot=True, fmt=".1f", cbar=False, ax=axes[1][0])
    axes[1][0].set_xlabel('')
    axes[1][0].set_ylabel('')
    sns.heatmap(d_rho_pivot_n_alpha, cmap='binary', annot=True, fmt=".1f", cbar=False, ax=axes[1][1])
    axes[1][1].set_xlabel('')
    axes[1][1].set_ylabel('')
    sns.heatmap(d_rho_pivot_mu_alpha, cmap='binary', annot=True, fmt=".1f", cbar=False, ax=axes[1][2])
    axes[1][2].set_xlabel('')
    axes[1][2].set_ylabel('')

    # Create the heatmaps for 'best_rho'
    sns.heatmap(best_rho_pivot_n_mu, cmap='binary', annot=True, fmt=".1f", cbar=False, ax=axes[2][0])
    axes[2][0].set_xlabel('')
    axes[2][0].set_ylabel('')
    sns.heatmap(best_rho_pivot_n_alpha, cmap='binary', annot=True, fmt=".1f", cbar=False, ax=axes[2][1])
    axes[2][1].set_xlabel('')
    axes[2][1].set_ylabel('')
    sns.heatmap(best_rho_pivot_mu_alpha, cmap='binary', annot=True, fmt=".1f", cbar=False, ax=axes[2][2])
    axes[2][2].set_xlabel('')
    axes[2][2].set_ylabel('')

    axes[0, 0].set_ylabel('Generations')
    axes[1, 0].set_ylabel('Diversity Ratio')
    axes[2, 0].set_ylabel('Best Ratio')

    plt.tight_layout()
    plt.savefig('heatmap_2.pdf')


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    get_heatmap()
