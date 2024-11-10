import seaborn as sns
import matplotlib.pyplot as plt

def split_category(df, new_col, old_col):
    df[new_col] = df[old_col].str.split(',')
    df_modified_explode = df.explode(new_col)
    df_modified_explode[new_col] = df_modified_explode[new_col].str.strip()
    return df_modified_explode

def group_other_categories(df, col, cat_list):
    df[col] = df[col].apply(lambda x: x.capitalize() if x in cat_list else 'Other Categories')
    return df

def plot_each_subjects_analysis(title, df, sub1_col, sub2_col, sub3_col, sub4_col, color, order=None):
    fig, ax = plt.subplots(2,2, figsize=(10,6))
    fig.suptitle(title, fontsize=16)

    sns.countplot(data=df, x=sub1_col, ax=ax[0,0], color=color, order=order, width=0.5, edgecolor='black')
    ax[0,0].set_title('Teching Effectiveness')
    ax[0,0].bar_label(ax[0,0].containers[0])
    ax[0,0].set_xlabel('Effective Rating')
    ax[0,0].set_ylabel('Number of Responses')

    require_cat = ['Yes', 'No', 'Maybe']
    sns.countplot(data=df, x=sub2_col, ax=ax[0,1], color=color, order=require_cat, width=0.5, edgecolor='black')
    ax[0,1].set_title("Training Time Sufficiency")
    ax[0,1].bar_label(ax[0,1].containers[0])
    ax[0,1].set_xlabel('Students\' Choice')
    ax[0,1].set_ylabel('')

    sns.countplot(data=df, x=sub3_col, ax=ax[1,0], color=color, order=order, width=0.5, edgecolor='black')
    ax[1,0].set_title('Content Satisfaction')
    ax[1,0].bar_label(ax[1,0].containers[0])
    ax[1,0].set_xlabel('Content Satisfaction Rating')
    ax[1,0].set_ylabel('Number of Response')

    sns.countplot(data=df, x=sub4_col, ax=ax[1,1], color=color, order=order, width=0.5, edgecolor='black')
    ax[1,1].set_title('Students Improvement Rating')
    ax[1,1].bar_label(ax[1,1].containers[0])
    ax[1,1].set_xlabel('Improvement Rating')
    ax[1,1].set_ylabel('')

    for axis in ax.flat:
        axis.set_ylim(0, 25)
        
    plt.tight_layout(rect=[0, 0, 1, 0.98]) 
    plt.show()