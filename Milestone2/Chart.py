import matplotlib.pyplot as pyplot
import numpy as np
from FileIO import FileIO
from WeatherAnalyzer import WeatherAnalyzer

class Chart:
        # Defines function of drawLineChart
        # Line Chart Minimum Temperature of 1990-2019 Annually
        # Line Chart Maximum Temperature of 1990-2019 Annually
    def drawLineChart(self,x,y,title,xlabel,ylabel):
        # Distinguishes between figures by assigning numerical values
        pyplot.figure()
        # Describes plot and provides insight into individual and dependent variables
        pyplot.title(title)
        # States array plotted on y-axis
        pyplot.ylabel(ylabel)
        # States array plotted on x-axis
        pyplot.xlabel(xlabel)
        # Highlights important data points by placing a marker
        pyplot.plot(x,y,marker='o')
        # Uses matplotlib.pyplot to display the Line Chart
        pyplot.show()
        
        # Defines function of drawBarChart
        # Bar Chart Average Snowfall between 1990-2019 Annually
        # Bar Chart Average Temperature between 1990-2019 Annually
    def drawBarChart(self,x,y,title,xlabel,ylabel):
        # Centers data about y-axis labels with median values at the center
        pyplot.bar(x,y,align='center',alpha=0.5)
        # States array plotted on y-axis
        pyplot.ylabel(ylabel)
        # States array plotted on x-axis
        pyplot.xlabel(xlabel)
        # Describes plot and provides insight into individual and dependent variables
        pyplot.title(title)
        # Uses matplotlib.pyplot to display the Bar Chart
        pyplot.show()

