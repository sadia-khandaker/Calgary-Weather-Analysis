import numpy as np

class FileIO:
    file_name = "Term_project\CalgaryWeather.csv"
    dataTable = np.loadtxt(file_name,delimiter=',',skiprows=1,usecols=(0,1,2,3,4), dtype=np.float)