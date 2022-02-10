from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_ex1(ex_1_values):
    fig, axs = plt.subplots(ncols=4, nrows=2, figsize=(16, 6))
    for i, x in enumerate(ex_1_values):
        ax = axs.flat[i]
        sns.heatmap(x, ax=ax)
    axs.flat[-1].remove()
    #fig.savefig('ex1.png')
    plt.show()
    plt.close('all')
    
def plot_ex2(ex_2_values):
    fig, axs = plt.subplots(ncols=2, figsize=(16, 6))
    for i, x in enumerate(ex_2_values[:2]):
        ax = axs.flat[i]
        sns.heatmap(x, ax=ax)
    #fig.savefig('ex2.png')
    plt.show()
    plt.close('all')
    print(ex_2_values[2:])
    
def plot_ex3(uniform_sample, normal_sample, normal_sample_3d):
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(121)
    ax.set_xlim([0,55])
    ax.set_ylim([0,55])
    sns.scatterplot(x=uniform_sample[:,0], y=uniform_sample[:,1], ax=ax)
    sns.scatterplot(x=normal_sample[:,0], y=normal_sample[:,1], ax=ax)
    ax = fig.add_subplot(122, projection='3d')
    ax.scatter(normal_sample_3d[:,0], normal_sample_3d[:,1], normal_sample_3d[:,2])
    ax.view_init(20, 340)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    #fig.savefig('ex3.png')
    plt.show()
    plt.close('all')
    
def plot_ex4(interventions_unique, drugs, trials):
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(221)
    g = sns.countplot(y = trials['age_clean'].sum(), ax=ax)
    for p in g.patches: 
        label = '0' if np.isnan(p.get_width()) else str(int(p.get_width()))
        ax.annotate(f'{label} ', (p.get_x() + p.get_width(), p.get_y() + p.get_height()/2),
                    ha='right', va='center', fontsize=9, xytext=(0, 0),
                    textcoords='offset points', color='white', weight='black')
    ax.set_ylabel('Clinical Trials')
    ax.set_ylabel('Age')
    ax = fig.add_subplot(222)
    g = sns.countplot(data = trials, x='Phases', ax=ax)
    for p in g.patches: 
        label = '0' if np.isnan(p.get_height()) else str(int(p.get_height()))
        ax.annotate(f'{label} ', (p.get_x() + p.get_width()/2, p.get_y() + p.get_height()),
                    ha='center', va='top', fontsize=9, xytext=(0, 0),
                    textcoords='offset points', color='white', weight='black')
    fig.savefig('ex4.png')
    ax = fig.add_subplot(212)
    dates = trials[['date']].copy()
    dates['count'] = 1
    dates.set_index('date', inplace=True)
    sns.lineplot(data=dates.sort_index().cumsum().reset_index(), x='date', y='count', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('number of clinical trials')
    fig.savefig('ex4.png')
    plt.show()
    plt.close('all')
    print(f'Number of Interventions: {len(interventions_unique)}')
    print(f'Number of Drugs: {len(drugs)}')
    
def plot_ex5(drugbank_wide, drugbank):
    fig = plt.figure(figsize = (20,8))
    ax = fig.add_subplot(221)
    sns.countplot(data=drugbank_wide, y='Top ATC', order=drugbank_wide.value_counts('Top ATC').index, ax=ax)
    ax.set_xlabel('Number of Drugs')
    ax = fig.add_subplot(222)
    d = drugbank[drugbank['variable'] == 'Group']
    sns.countplot(data=d, y='value', order=d.value_counts('value').index, ax=ax)
    ax.set_ylabel('Approval Status')
    ax.set_xlabel('Number of Drugs')
    ax = fig.add_subplot(212)
    sns.countplot(data=drugbank_wide, x='Target Count', ax=ax)
    ax.set_yscale('log')
    ax.tick_params(axis='x', which='both', rotation=90)
    fig.savefig('ex5.png')
    plt.show()
    plt.close('all')