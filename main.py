class TimeConverter:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds
    def __del__(self):
        print(f"Об'єкт TimeConverter:{self.__hours}: {self.__minutes}: {self.__seconds}, знищено")
    def get_hours(self):
        return self.__hours
    def set_hours(self, hours):
        self.__hours=hours
    def get_minutes(self):
        return self.__minutes
    def set_minutes(self,minutes):
        self.__minutes=minutes
    def get_seconds(self):
        return self.__seconds
    def set_seconds(self, seconds):
        self.__seconds=seconds        
    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"
    def __repr__(self):
        return f"TimeConverter(hours={self.__hours}, minutes={self.__minutes}, seconds={self.__seconds})"
    def outputConvertedTime(self, total_seconds=None):
        if total_seconds is None:
            return self.__hours*3600+self.__minutes*60+self.__seconds
        else:
            h=total_seconds//3600
            m=(total_seconds%3600)//60
            s=total_seconds%60
            return f"{h:02d}:{m:02d}:{s:02d}"
def main():
    t1=TimeConverter(2,45,30)
    print("Вивід t1 (str):",t1)
    print("Вивід t1 (repr):", repr(t1))

    sec=t1.outputConvertedTime()
    print("Час t1 у секундах:", sec)

    sec_value=1000
    converted_time=t1.outputConvertedTime(sec_value)
    print(f"{sec_value} секунд у форматі hh:mm:ss", converted_time)

    t2=TimeConverter()
    t2.set_hours(1)
    t2.set_minutes(15)
    t2.set_seconds(5)
    print("Об'єкт t2 після сетерів:", t2)

if __name__=="__main__":
    main()
