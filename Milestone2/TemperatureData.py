from Date import Date

class TemperatureData:
    def __init__(self,a,):
        self.a = a
        self.month = self._Date_(2)
        self.year = self._Date_(1)
        self.min  = self.giveMinTemp()
        self.max = self.giveMaxTemp()
        self.snow = self.giveSnowFall()

    def _Date_(self, b):
        _date_object_ = Date(self.a[0], self.a[1])
        if b == 1:
            return _date_object_.year 
        if b == 2:
            return _date_object_.month
    def giveMinTemp(self): 
        minTemperature = self.a[3]
        return minTemperature

    def giveMaxTemp(self):
        maxTemperature = self.a[2]
        return maxTemperature

    def giveSnowFall(self):
        snowFall = self.a[4]
        return snowFall

