"""
This program is written for trend analysis of a time series, e.g. COVID-19.
"""

__author__='Najmeh Kaffashzadeh'
__author_email__ = 'najmeh.kaffashzadeh@gmail.com'

# import standard data science python libraries
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib
import matplotlib.pyplot as plt

font = {'family':'serif','weight':'normal','size':10}
matplotlib.rc('font',**font)


class TrendAnalysis:


    name = 'trend analysis'

    def __init__(self, df=None):
        """
        This is to initialized the BoxPlot class.
        """
        # input data
        self.__df=df
        # trend
        self.__trend = None
        # residual
        self.__resid = None

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
        plt.savefig('../examples/trend_analysis_plot_COVID19.png', bbox_inches='tight')
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

    def plot(self):
        """
        It plots the results.
        """
        fig, ax = plt.subplots(1, 2, figsize=(25, 5))
        self.__df['Death'].plot(ax=ax[0], kind='bar', use_index=False)
        plt.xticks([], [])
        self.__trend.plot(ax=ax[0], title='', color='r', linewidth=2, legend=False)
        ax[0].bar(self.__df.index, self.__df['Death'])
        ax[0].set_ylabel('number of death per day')
        # second plot
        self.__trend.plot(ax=ax[1], title='', color='r', linewidth=2, legend=False)
        self.__resid.plot(ax=ax[1], title='', color='g', linewidth=2, legend=False)
        plt.legend(['trend', 'residual'], loc='best', bbox_to_anchor=(0.2, 0.5, 1.05, 0.5))
        plt.suptitle('Trend Analysis of COVID-19 death in UK', fontweight='bold', fontsize=14)
        self.save_fig(fig=fig)

    def estimate_trend(self):
        """
        It estimates trends.

        Note:
            Here, an additive model has been used.
        """
        spectral = seasonal_decompose(self.__df, model='additive')
        self.__trend = spectral.trend
        self.__resid = spectral.resid


    def run(self):
        """
        It runs the script.
        """
        self.estimate_trend()
        self.plot()


if __name__=='__main__':
    df = pd.read_csv('../examples/UK_death_COVID19.csv', header=0, index_col=0, parse_dates=True, sep='\s+')
    new_index = pd.date_range(start=df.index[0], end=df.index[-1], freq='D')
    TrendAnalysis(df=df).run()
