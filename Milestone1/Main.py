import sys
from FileIO import FileIO
from WeatherAnalyzer import WeatherAnalyzer
from TemperatureData import TemperatureData

def Menu_Screen():
    print("(1) Get Minimum Temperature of 1990-2019")
    print("(2) Get Maximum Temperature of 1990-2019")
    print("(3) Get Minimum Temperature of 1990-2019 Annually")
    print("(4) Get Maximum Temperature of 1990-2019 Annually")
    print("(5) Get Average Snowfall between 1990-2019 Annually")
    print("(6) Exit")
    A = int(input("Which choice would you like to see?"))
    return A

def main():
    choice = Menu_Screen()
    x = True
    while x:
        while choice in [1,2,3,4,5,6]:
            data_ = FileIO() 
            data = data_.dataTable 
            TDL = [] 
            for j in range(0,len(data)): 
                Temp_object_ = TemperatureData(data[j])
                TDL.append(Temp_object_)
            DataAnalysis = WeatherAnalyzer(TDL)

            if choice == 1:
                print(DataAnalysis.getMinTemp())
            elif choice == 2:
                print(DataAnalysis.getMaxTemp())
            elif choice == 3:
                print(DataAnalysis.getMinTempAnnually())
            elif choice == 4:
                print(DataAnalysis.getMaxTempAnnually())
            elif choice == 5:
                print(DataAnalysis.getAvgSnowFallAnnually())
            else:
                print("Thank you. Bye")
                sys.exit()

            choice = Menu_Screen()
        choice = int(input("Invalid entry, please try again."))

if __name__ == "__main__":
    main()

