import matplotlib.pyplot as plt

def change_plot_defaults ():
    plt.rcParams['font.family'] = ['Arial']
    plt.rcParams['text.color'] = 'xkcd:black'
    plt.rcParams['axes.edgecolor'] = 'xkcd:dark gray'
    plt.rcParams['axes.labelcolor'] = 'xkcd:black'
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['xtick.color'] = 'xkcd:dark gray'
    plt.rcParams['ytick.color'] = 'xkcd:dark gray'
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.fontsize'] = 14
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
    plt.rcParams['scatter.edgecolors'] = 'xkcd:dark gray'
    plt.rcParams['savefig.format'] = 'pdf'
    plt.rcParams['savefig.transparent'] = True
    plt.rcParams['legend.handletextpad'] = 1

def grid_maker(data,fig):
    plt.figure(fig)
    for i in range(len(data)):
        plt.plot([-.5,len(data[0])-0.5],[i-0.5,i-0.5],'-',color='xkcd:dark gray',linewidth=0.5)
    for j in range(len(data[0])+1):
        plt.plot([j-0.49,j-0.49],[-0.5,len(data)-0.5],'-',color='xkcd:dark gray',linewidth=0.5)
