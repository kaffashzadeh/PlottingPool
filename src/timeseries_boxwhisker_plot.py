"""
This program is written for plotting a box plot along with the scatter data points.
"""

__author__='Najmeh Kaffashzadeh'
__author_email__ = 'najmeh.kaffashzadeh@gmail.com'

# import standard data science python libraries
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family': 'serif', 'weight': 'normal', 'size': 12}
matplotlib.rc('font', **font)


class TimeSeriesBoxWhiskerPlot:

    name = 'time series and box whisker plots'

    def __init__(self):
        """
        This is to initialized the BoxPlot class.
        """
        # input data
        self.__df = None
        # face colours
        self.__fcs = ['w', 'w', 'w', 'w','w']
        # edge colours
        self.__ecs = ['royalblue', 'lime', 'tomato', 'magenta', 'red']

    def __repr__(self):
        """
        It represent the class name.
        """
        return "%s(%r)" % (self.__class__, self.__dict__)

    def save_fig(self, fig=None):
        """
        It save and close the figure.

        Args:
            fig(object): figure to save
        """
        plt.savefig('../examples/timeseries_boxwhisker_temp_ozone_cve.png', bbox_inches='tight')
        plt.close()

    def make_subplot(self, nrows=1, ncols=2):
        """
        It makes subplot.

        Args:
            nrows(int): number of rows
            ncols(int): number of columns

        Return:
               fig and axes objects
        """
        fig, axes = plt.subplots(nrows, ncols, figsize=(15., 8.), facecolor='white')
        return fig, axes

    def plot_box_whisker(self, ax=None):
        """
        It plots box whisker.

        Args:
             ax(obj): the axis object
        """
        # column name (here disease)
        dnames = list(self.__df.columns)
        # values
        vals = [self.__df[dnames[i]].values for i in range(0, len(dnames))]
        # face colours
        fcs = [self.__fcs[i] for i in range(0, len(dnames))]
        # edge colours
        ecs = [self.__ecs[i] for i in range(0, len(dnames))]
        # box plot
        bp = ax.boxplot(vals, patch_artist=True, showmeans=True,
                        medianprops=dict(linestyle='-', linewidth=1.5, color='orange'),
                        meanprops=dict(marker='D', markeredgecolor='black',
                                            markerfacecolor='firebrick'))
        plt.setp(bp['fliers'], markersize=1.0)
        for patch, fc, ec in zip(bp['boxes'], fcs, ecs):
             patch.set_facecolor(fc)
             patch.set_edgecolor(ec)
             patch.set_linewidth(2)

    def add_scatter(self, ax=None):
        """
        It adds scatter next to the boxes.

        Args:
             ax(obj): the axis object
        """
        dnames = list(self.__df.columns)
        for val, idx, fc, ec in [[i+0.7, i, self.__fcs[i], self.__ecs[i]] for i in range(0, len(dnames))]:
            ax.scatter(np.full(shape=len(self.__df), fill_value=val),
                       self.__df[dnames[idx]],
                       color=fc, edgecolor=ec, marker='o', s=10)

    def customize_xticks(self, ax=None):
        """
        It customizes the xticks).

        Args:
            ax(obj): the axis object
        """
        dnames = list(self.__df.columns)
        ax.set_xticklabels(dnames)

    def run(self, df1=None, df2=None):
        """
        It run the BoxPlot.

        Args:
            df1(pd.DataFrame): first input data
            df2(pd.DataFrame): second input data
        """
        # make a figure and subplots
        fig, axes = self.make_subplot(nrows=1, ncols=2)
        ax = axes[0]
        self.__df = df1
        ax.set_title('ground-level ozone', fontweight='bold')
        self.plot_box_whisker(ax=ax)
        self.add_scatter(ax=ax)
        self.customize_xticks(ax=ax)
        ax.set_ylim(-50, 2100)
        ax.set_ylabel('number of the CVEs occurance')
        ax.set_xlabel('CVEs lenght (t)')
        ax = axes[1]
        self.__df = df2
        ax.set_title('atmospheric temperature', fontweight='bold')
        self.plot_box_whisker(ax=ax)
        self.add_scatter(ax=ax)
        self.customize_xticks(ax=ax)
        ax.set_ylabel('number of the CVEs occurance')
        ax.set_xlabel('CVEs lenght (t)')
        ax.set_ylim(-50, 2100)
        plt.suptitle('an experiment using 166896 measured data points', fontweight='bold', fontsize=16)
        self.save_fig(fig=fig)


if __name__ == '__main__':
    df1 = pd.read_csv('../examples/cve_occurance_ozone.csv', header=0, sep='\t')
    df2 = pd.read_csv('../examples/cve_occurance_temp.csv', header=0, sep='\t')
    TimeSeriesBoxWhiskerPlot().run(df1=df1, df2=df2)
