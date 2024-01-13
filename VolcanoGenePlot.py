import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    input_path = r'/home/mb20879/gene_exp.diff'

    data = pd.read_csv(input_path, sep='\t', decimal='.')
    data = data[~data['log2(fold_change)'].isin([np.inf, -np.inf])]

    # Add a column for -log10(q_value)
    data['-log10(q_value)'] = -np.log10(data['q_value'])

    # Define thresholds for significance and log2 fold change
    significance_threshold = 0.05  # q-value threshold for significance
    fold_change_threshold = 1  # log2 fold change threshold

    # Identify significant genes
    data['significant'] = (data['q_value'] < significance_threshold)
    data['upregulated'] = (data['log2(fold_change)'] < -fold_change_threshold) & data['significant']
    data['downregulated'] = (data['log2(fold_change)'] > fold_change_threshold) & data['significant']
    data['not_significant'] = ~data['significant']

    # Plotting the volcano plot with separate categories
    plt.figure(figsize=(10, 8))

    # Non-significant genes
    plt.scatter(data.loc[data['not_significant'], 'log2(fold_change)'],
                data.loc[data['not_significant'], '-log10(q_value)'],
                color='grey', alpha=0.7, label='Not Sig', s=80)

    # Upregulated genes
    plt.scatter(data.loc[data['upregulated'], 'log2(fold_change)'],
                data.loc[data['upregulated'], '-log10(q_value)'],
                color='red', alpha=0.3, label='Upregulated', s=80)

    # Downregulated genes
    plt.scatter(data.loc[data['downregulated'], 'log2(fold_change)'],
                data.loc[data['downregulated'], '-log10(q_value)'],
                color='blue', alpha=0.3, label='Downregulated', s=80)

    # Highlighting significant genes with labels
    for i, row in data[(data['upregulated'] | data['downregulated'])].iterrows():
        plt.annotate(row['gene'], xy=(row['log2(fold_change)'], row['-log10(q_value)']),
                     xytext=(0, 8), textcoords='offset points',
                     ha='center', va='bottom', fontsize=10)

    # Adding labels and title
    plt.xlabel('log2(Fold Change)', fontsize=12)
    plt.ylabel('-log10(q-value)', fontsize=12)
    plt.axhline(-np.log10(significance_threshold), color='black', linewidth=0.5, linestyle='--')
    plt.axvline(fold_change_threshold, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(-fold_change_threshold, color='black', linewidth=0.5, linestyle='--')
    plt.legend(loc='upper right', fontsize=12)
    plt.grid(False)
    plt.show()
