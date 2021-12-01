import numpy as np

class FileIO:
    def __init__(self):
        self.file_name = "CalgaryWeather.csv"
        self.dataTable = self.readWeather()

    def readWeather(self):    
        dataTable = np.loadtxt(self.file_name,delimiter=',',skiprows=1,usecols=(0,1,2,3,4), dtype=np.float)
        return dataTable