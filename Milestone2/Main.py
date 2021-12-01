import sys
from FileIO import FileIO
from WeatherAnalyzer import WeatherAnalyzer
from TemperatureData import TemperatureData
from Chart import Chart
import numpy as np
import matplotlib.pyplot as pyplot


def Menu_Screen():
    print("(1) Get Minimum Temperature of 1990-2019")
    print("(2) Get Maximum Temperature of 1990-2019")
    print("(3) Get Minimum Temperature of 1990-2019 Annually")
    print("(4) Get Maximum Temperature of 1990-2019 Annually")
    print("(5) Get Average Snowfall between 1990-2019 Annually")
    print("(6) Get Average Temperature between 1990-2019 Annually")
    print("(7) Line Chart Minimum Temperature of 1990-2019 Annually")
    print("(8) Line Chart Maximum Temperature of 1990-2019 Annually")
    print("(9) Bar Chart Average Snowfall between 1990-2019 Annually")
    print("(10) Bar Chart Average Temperature between 1990-2019 Annually")
    print("(11) Exit")
    A = int(input("Which choice would you like to see?"))
    return A

def main():
    choice = Menu_Screen()
    x = True
    while x:
        while choice in [1,2,3,4,5,6,7,8,9,10,11]:
            data_ = FileIO() 
            data = data_.dataTable
            TDL = [] 
            for j in range(0,len(data)): 
                Temp_object_ = TemperatureData(data[j])
                TDL.append(Temp_object_)
            DataAnalysis = WeatherAnalyzer(TDL)

            chart = Chart()
            Year_List = np.array([])
            for t in range(1990,2020):
                Year_List = np.append(Year_List,t) 
            if choice == 1:
                print(DataAnalysis.getMinTemp())
            elif choice == 2:
                print(DataAnalysis.getMaxTemp())
            elif choice == 3:
                print(DataAnalysis.getMinTempAnnually(1))
            elif choice == 4:
                print(DataAnalysis.getMaxTempAnnually(1))
            elif choice == 5:
                print(DataAnalysis.getAvgSnowFallAnnually(1))
            elif choice == 6:
                print(DataAnalysis.getAvgTempAnnually(1))
            elif choice == 7:
                Y_Cordinate = (DataAnalysis.getMinTempAnnually(2))
                chart.drawLineChart(Year_List, Y_Cordinate, "Minimum Temperature of 1990-2019 Annually", "Year", "Temperature (C)")
            elif choice == 8:
                Y_Cordinate = (DataAnalysis.getMaxTempAnnually(2))
                chart.drawLineChart(Year_List, Y_Cordinate, "Maximum Temperature of 1990-2019 Annually", "Year", "Temperature (C)")
            elif choice == 9:
                Y_Cordinate = (DataAnalysis.getAvgSnowFallAnnually(2))
                chart.drawBarChart(Year_List, Y_Cordinate, "Average Snowfall between 1990-2019 Annually","Year", "Average Snowfall (cm)")
            elif choice == 10:
                Y_Cordinate = (DataAnalysis.getAvgTempAnnually(2))
                chart.drawBarChart(Year_List, Y_Cordinate, "Average Temperature between 1990-2019 Annually", "Year", "Average Temperature (C)")
            else:
                print("Thank you. Bye.")
                sys.exit()

            choice = Menu_Screen()
        choice = int(input("Invalid entry, please try again."))

if __name__ == "__main__":
    main()
