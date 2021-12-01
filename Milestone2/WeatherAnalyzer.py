import numpy as np
        #Return the class method for WeatherAnalyzer
class WeatherAnalyzer:
        #Initilization
    def __init__(self,_List_):
        self._List_ = _List_

        #Defining the variable getMinTemp
    def getMinTemp(self):
        # This function analyzes each specific row of the table data and adds the minimum temperature of each given year to the
        # empty array we created, which then creates an array that returns with the minimum temperature of each year
        minimumTempL = np.array([])

        # Initialize Loop
        for i in range(0,len(self._List_)):
            Object = self._List_[i].giveMinTemp() 
            minimumTempL = np.append(minimumTempL, Object)
        
        # X is defined as a function that uses numpy to calculate the minimum temperature in the entire data set
        x = np.min(minimumTempL)

        return "Minimum Temperature:"+ str(x)

        #Defining the variable getMinTempAnnually
    def getMinTempAnnually(self,t):

        self.t = t
        # 2 empty arrays are created to be used in the function
        MinimumAnnualT_ = np.array([])
        _List_Info_ = np.array([])

        # From Jan-Dec of each year
        A = 0 
        B = 12

        for i in range(0,30):
            # creating an empty array
            n_AnnualTemp_List = np.array([])
            # Because 2019 only has 11 months of data we cannot go over the 359th month other wise the data would be out of range
            if i == 29: 
                B = 359 

            for j in range(A,B):

                Object = self._List_[j].giveMinTemp() 
                n_AnnualTemp_List = np.append(n_AnnualTemp_List, Object)

            # Defining years as a 2D array of dates with corresponding n_AnnualTemp_List
            # First starts with Min Temp and it splits it up as 12 monthly values for a specific year between 1990-2019
            # Next you obtain the corresponding dates of n_AnnualTemp_List values for each month
            # Yearly_Temperature_ takes the min of the n_AnnualTemp_List for each month specific to a year, accurate to 4 decimals
            years = self._List_[j]._Date_(1)
            Yearly_Temperature_ = [f"{years:.0f} : {np.min(n_AnnualTemp_List):.4f}"]
            # MinimumAnnualT_ is an empty array we created and the calculated values of Yearly_Temperature_ is appended to it
            MinimumAnnualT_ = np.append(MinimumAnnualT_, Yearly_Temperature_)
            # MinimumAnnualT_ is an appended array where calculated values of Yearly_Temperature_ are present
            _List_Info_ = np.append(_List_Info_, np.min(n_AnnualTemp_List))
        
            A += 12  
            B += 12

            # Categorizing data per annum
        if t == 1:
            return MinimumAnnualT_
        elif t == 2:
            return _List_Info_

        #Defining the variable getMinTemp   
    def getMaxTemp(self):
        # This function analyzes each specific row of the table data and adds the maximum temperature of each given year to the
        # empty array we created, which then creates an array that returns with the maximum temperature of each year
        M_T_L = np.array([])

        # Initialize Loop
        for i in range(0,len(self._List_)):
            Object = self._List_[i].giveMaxTemp()
            M_T_L = np.append(M_T_L, Object)  

        # X is defined as a function that uses numpy to calculate the maximum temperature in the entire data set
        x = np.max(M_T_L)
        
        return "Maximum Temperature:"+ str(x)

        #Defining the variable getMaxTempAnnually
    def getMaxTempAnnually(self,t):

        self.t = t
        # 2 empty arrays are created to be used in the function
        _Max_Annual_T = np.array([])
        _List_Info_ = np.array([])

        # From Jan-Dec of each year
        A = 0
        B = 12

        for i in range(0,30):
            # creating an empty array
            M_AnnualTemp_List = np.array([])
            # Because 2019 only has 11 months of data we cannot go over the 359th month other wise the data would be out of range
            if i == 29:
                B = 359

            for j in range(A,B):
                Object = self._List_[j].giveMaxTemp()
                M_AnnualTemp_List = np.append(M_AnnualTemp_List, Object)

            # Defining years as a 2D array of dates with corresponding M_AnnualTemp_List
            # First starts with MaxTemp and it splits it up as 12 monthly values for a specific year between 1990-2019
            # Next you obtain the corresponding dates of M_AnnualTemp_List values for each month
            # Yearly_Temperature_ takes the Max of the M_AnnualTemp_List for each month specific to a year, accurate to 4 decimals   
            years = self._List_[j]._Date_(1)
            Yearly_Temperature_ = [f"{years:.0f} : {np.max(M_AnnualTemp_List):.4f}"]
            # _Max_Annual_T is an empty array we created and the calculated values of Yearly_Temperature_ is appended to it
            _Max_Annual_T = np.append(_Max_Annual_T, Yearly_Temperature_)
            # _Max_Annual_T is an appended array where calculated values of Yearly_Temperature_ are present
            _List_Info_ = np.append(_List_Info_, np.max(M_AnnualTemp_List))

            A += 12
            B += 12
            
            # Categorizing data per annum
        if t == 1:
            return _Max_Annual_T
        elif t == 2:
            return _List_Info_

        #Defining the variable getAvgSnowFallAnnually
    def getAvgSnowFallAnnually(self,t): 

        self.t = t
        # 2 empty arrays are created to be used in the function
        _S_F_L = np.array([])
        _List_Info_ = np.array([])

        # From Jan-Dec of each year
        A = 0
        B = 12

        for i in range(0,30):
            # creating an empty array 
            _Annual_Snow_array = np.array([])
            # Because 2019 only has 11 months of data we cannot go over the 359th month other wise the data would be out of range
            if i == 29:
                B = 359
            
            for j in range(A,B):
                Object = self._List_[j].giveSnowFall()
                _Annual_Snow_array = np.append(_Annual_Snow_array, Object)

            # Defining years as a 2D array of dates with corresponding _Annual_Snow_array
            # First starts with annual snowfall and it splits it up as 12 monthly values for a specific year between 1990-2019
            # Next you obtain the corresponding dates of _Annual_Snow_array values for each month
            # _Yearly_Snow_ takes the average of the _Annual_Snow_array for each month specific to a year, accurate to 4 decimals
            years = self._List_[j]._Date_(1)
            _Yearly_Snow_ = [f"{years:.0f} : {np.mean(_Annual_Snow_array):.4f}"]
            # _S_F_L is an empty array we created and the calculated values of _Yearly_Snow_ is appended to it 
            _S_F_L = np.append(_S_F_L, _Yearly_Snow_)
            # _S_F_L is an appended array where calculated values of _Yearly_Snow_ are present
            _List_Info_ = np.append(_List_Info_, np.mean(_Annual_Snow_array))

            A += 12
            B += 12

            # Categorizing data per annum
        if t == 1:
            return _S_F_L
        elif t == 2:
            return _List_Info_

        # Defining the variable getAvgTempAnnually
    def getAvgTempAnnually(self,t):

        self.t = t
        # 2 empty arrays are created to be used in the function
        AnnualTemp_AvgL = np.array([])
        _List_Info_ = np.array([])

        # From Jan-Dec of each year
        A = 0
        B = 12

        for i in range(0,30):
            # creating an empty array
            AvgTemp_Array = np.array([])
            # Because 2019 only has 11 months of data we cannot go over the 359th month other wise the data would be out of range
            if i == 29:
                B = 359

            for j in range(A,B):
                Object = (self._List_[j].giveMaxTemp() + self._List_[j].giveMinTemp())/2
                AvgTemp_Array = np.append(AvgTemp_Array, Object)

            # Defining years as a 2D array of dates with corresponding AvgTemp_Array
            # First starts with annual average temperature and it splits it up as 12 monthly values for a specific year between 1990-2019
            # Next you obtain the corresponding dates of AvgTemp_Array values for each month
            # _Yearly_AvgTemp_ takes the average of the AvgTemp_Array for each month specific to a year, accurate to 4 decimals
            years = self._List_[j]._Date_(1)
            _Yearly_AvgTemp_ = [f"{years:.0f} : {np.mean(AvgTemp_Array):.4f}"]
            # AnnualTemp_AvgL is an empty array we created and the calculated values of _Yearly_AvgTemp_ is appended to it 
            AnnualTemp_AvgL = np.append(AnnualTemp_AvgL,_Yearly_AvgTemp_)
            # AnnualTemp_AvgL is an appended array where calculated values of _Yearly_AvgTemp_ are present
            _List_Info_ = np.append(_List_Info_, np.mean(AvgTemp_Array))

            A += 12
            B += 12

            # Categorizing data per annum
        if t == 1:
            return AnnualTemp_AvgL
        elif t == 2:
            return _List_Info_