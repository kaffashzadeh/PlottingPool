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

font = {'family':'serif','weight':'normal','size':10}
matplotlib.rc('font',**font)


class TimeSeriesBoxWhiskerPlot:


    name = 'time series and box whisker plots'

    def __init__(self):
        """
        This is to initialized the BoxPlot class.
        """
        # input data
        self.__df=None
        # face colours
        self.__fcs = ['w', 'w', 'w', 'w']
        # edge colours
        self.__ecs = ['royalblue', 'lime', 'tomato', 'magenta']

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
        plt.savefig('../examples/timeseries_boxwhisker_plot.png', bbox_inches='tight')
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
        fig, axes = plt.subplots(nrows, ncols, figsize=(16., 8.), facecolor='white')
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

    def run(self, df=None):
        """
        It run the BoxPlot.

        Args:
            df(pd.DataFrame): input data
        """
        # make a figure and subplots
        fig, axes = self.make_subplot(nrows=2, ncols=2)
        self.__df = df[['cold', 'flu', 'pneumonia', 'coronavirus']]
        ax = axes[0,0]
        self.__df.plot(ax=ax, color=self.__ecs)
        #ax.set_title('from 6 December 2019 to 6 March 2020', fontweight='bold')
        ax.set_ylabel('search volume (% per day)')
        ax = axes[1,0]
        self.plot_box_whisker(ax=ax)
        self.add_scatter(ax=ax)
        self.customize_xticks(ax=ax)
        ax.set_ylabel('search volume (% per day)')

        self.__df = df[['cold', 'flu', 'pneumonia']]
        ax = axes[0,1]
        self.__df.plot(ax=ax, color=self.__ecs)
        #ax.set_title('from 6 December 2019 to 6 March 2020', fontweight='bold')
        ax.set_ylabel('search volume (% per day)')
        ax = axes[1,1]
        self.plot_box_whisker(ax=ax)
        self.add_scatter(ax=ax)
        self.customize_xticks(ax=ax)
        ax.set_ylabel('search volume (% per day)')
        plt.suptitle('Trend data of the keywords searched in NAVER which is one of the largest portal in South Korea',
                     fontweight='bold', fontsize=14)
        self.save_fig(fig=fig)


if __name__=='__main__':
    df = pd.read_csv('../examples/coronavirusdataset/trend.csv', header=0, index_col=0)
    TimeSeriesBoxWhiskerPlot().run(df=df)
