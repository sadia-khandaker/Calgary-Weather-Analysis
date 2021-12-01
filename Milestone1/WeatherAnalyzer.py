import numpy as np

class WeatherAnalyzer:
    def __init__(self,_List_): 
        self._List_ = _List_
    def getMinTemp(self):
        minimumTempL = np.array([]) 
        for i in range(0,len(self._List_)):
            Object = self._List_[i].giveMinTemp() 
            minimumTempL = np.append(minimumTempL, Object) 
        x = np.min(minimumTempL) 
        return "Minimum Tempreature:"+ str(x)

    def getMinTempAnnually(self):
        MinimumAnnualT_ = np.array([]) 
        A = 0 
        B = 12
        for i in range(0,30): 
            AnnualTemp_List = np.array([])
            if i == 29: 
                B = 359 =
            for j in range(A,B): 
                Object = self._List_[j].giveMinTemp() 
                AnnualTemp_List = np.append(AnnualTemp_List, Object) 
            _Annual_Temp_ = [np.min(AnnualTemp_List)] 
            MinimumAnnualT_ = np.append(MinimumAnnualT_, _Annual_Temp_) 
            A += 12 
            B += 12
        return MinimumAnnualT_ 
    def getMaxTemp(self): 
        M_T_L = np.array([])
        for i in range(0,len(self._List_)):
            Object = self._List_[i].giveMaxTemp()
            M_T_L = np.append(M_T_L, Object)  
        x = np.max(M_T_L)
        
        return "Maximum Temperature:"+ str(x)

    def getMaxTempAnnually(self): 
        _Max_Annual_T = np.array([])
        A = 0
        B = 12
        for i in range(0,30):
            AnnualTemp_List = np.array([])
            if i == 29:
                B = 359
            for j in range(A,B):
                Object = self._List_[j].giveMaxTemp()
                AnnualTemp_List = np.append(AnnualTemp_List, Object)
        
            _Annual_Temp_ = [np.max(AnnualTemp_List)]
            _Max_Annual_T = np.append(_Max_Annual_T, _Annual_Temp_)
            A += 12
            B += 12
        return _Max_Annual_T

    def getAvgSnowFallAnnually(self): 
        _S_F_L = np.array([])
        A = 0
        B = 12
        for i in range(0,30):
            _Annual_Snow_array = np.array([])
            if i == 29:
                B = 359
            for j in range(A,B):
                Object = self._List_[j].giveSnowFall()
                _Annual_Snow_array = np.append(_Annual_Snow_array, Object)
            
            _Annual_Snow_ = [np.mean(_Annual_Snow_array)]
            _S_F_L = np.append(_S_F_L, _Annual_Snow_)
            A += 12
            B += 12
        return _S_F_L