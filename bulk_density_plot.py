import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# For Jenny's MS.

datafile = 'data/BD&OM.xlsx'

df_dict = pd.read_excel(datafile, sheet_name=None)

fig, (ax) = plt.subplots(
    nrows=5,
    ncols=3,
    sharex=True,
    sharey=True,
    figsize=(8,10),
    #figsize=(10, 15),

)

#fig.subplots_adjust(hspace=0.05, wspace=0.05)
fig.subplots_adjust(hspace=0.1, wspace=0.1)

ax = ax.flatten()
i = 0
for sheet in df_dict:
    df = df_dict[sheet]
    if sheet == 'Site1':
        # filter data
        indexNames = df[ (df['Subsite'] == '1A') & (df['Depth (cm)'] == '90-100') ].index
        df.loc[indexNames, 'Bulk Density (g cm-3)'] = np.nan
        #df = df.drop((df.loc[df['Subsite'] == '1A']) & (df.loc[df['Depth (cm)'] == '90-100']))

    df['subsite_letter'] = df['Subsite'].str[-1]
    for subsite in df['subsite_letter'].unique():
        z = df.loc[df['subsite_letter'] == subsite, 'Average Depth (cm)']
        bd = df.loc[df['subsite_letter'] == subsite, 'Bulk Density (g cm-3)']
        om = df.loc[df['subsite_letter'] == subsite, '% Organic Matter']
        ss = df.loc[df['subsite_letter'] == subsite, 'Subsite']

        lin1 = ax[i].plot(om.values, z.values,
                          label='Organic Matter',
                          linestyle='--',
                          linewidth=0.5,
                          marker='^',
                          markersize=4,
                          fillstyle='none',
                          color='k')

        ax[i].set_yticks( np.arange(0, 101, 20) )
        ax[i].set_ylim(ax[i].get_ylim()[::-1])
        ax[i].set_xlim(0,100)

        ax[i].text(88,95,
                   ss.unique()[0],
                   #fontweight='bold',
                   )
        ax2v = ax[i].twiny()
        lin2 = ax2v.plot(bd.values,z.values,
                         label='Bulk Density',
                         linestyle='-',
                         linewidth=0.5,
                         marker='o',
                         markersize=4,
                         color='k')
        ax2v.set_xlim(0,1)
        ax2v.xaxis.set_major_formatter(FormatStrFormatter('%g'))
        if i > 2:
            ax2v.get_xaxis().set_visible(False)
        if i < 12:
            ax[i].get_xaxis().set_visible(False)
        if i in [1,2,4,5,7,8,10,11,13,14]:
            ax[i].get_yaxis().set_visible(False)
        i += 1

#ax[i].legend
#lines =
lns = lin1+lin2
labs = [l.get_label() for l in lns]
ax[14].legend(lns, labs,
              bbox_to_anchor=(1.0, -0.6),
              loc="lower right",
              borderaxespad=0,
              ncol=1,
              frameon=False,
              fontsize='large')
#ax[14].legend(

for ax in ax.flat:
    ax.label_outer()

fig.text(0.52, 0.06,
         'Organic Matter (%)',
         ha='center',
         va='center',
         fontsize='x-large')

fig.text(0.52, 0.93,
         'Bulk Density (g cm$^{-3}$)',
         ha='center',
         va='center',
         fontsize='x-large')

fig.text(0.06, 0.5,
         'Depth (cm)',
         ha='center',
         va='center',
         rotation='vertical',
         fontsize='x-large')

plt.savefig('Figure2.png')
