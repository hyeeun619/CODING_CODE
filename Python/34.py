#날짜별 전력사용량
from abc import ABC, abstractmethod
electricity_usage = [
    {"date" : "2024-11-01", "usage": 12.5},
    {"date" : "2024-11-02", "usage": 15.3},
    {"date" : "2024-11-03", "usage": 10.8},
    {"date" : "2024-11-04", "usage": 14.2},
    {"date" : "2024-11-05", "usage": 13.6},
]

# 추상클래스
class ElectricityData(ABC): # 추상클래스
    def __init__(self, usage_data, total_usage = 0):
        self._usage_data = usage_data # 전력사용량 리스트 (날짜, 사용량)
        self._total_usage = total_usage # 총 사용량

    @property
    def usage_data(self):
        return self._usage_data
    
    @property
    def total_usage(self):
        return self._total_usage
    
    @usage_data.setter
    def usage_data(self, new_data):
        self._total_usage = new_data

    @total_usage.setter
    def total_usage(self, new_total):
        self._total_usage = new_total


    # 추상 메서드 : 선언만 되어 있고, 구현하지 않은 메서드드
    @abstractmethod
    def calculate_total_usage(self):
        pass
    
    @abstractmethod
    def get_usage_on_data(self,data):
        pass

    # 일반 메서드
    def add_usage(self, date, usage):
        # self._usage_data 리스트에 ({"date": date, "usage": usage}) 형식으로 요소 추가가
        self._usage_data.append({"date": date, "usage": usage})

    def remove_usage(self, date): # date 매개변수: "2024-11-02"
        self._usage_data = [i for i in self._usage_data if i["date"] != date]

class HomeElectricityData(ElectricityData): #부모클래스(추상클래스)를 상속받는 자식클래스
    # (부모클래스에 있는) 추상 메서드 구현
    def calculate_total_usage(self):
        usage_list = [i["usage"] for i in self._usage_data]
        # [12.5, 15.3, 10.8, 14.2, 13.6]
        self._total_usage = sum(usage_list)

    def get_usage_on_data(self, date):
        for i in self.usage_data:
            if i["date"] == date:
                return i["usage"]
            
    # 클래스 메서드: 인스턴스(객체)가 아닌 "클래스"가 주인인 메서드 
    @classmethod
    def filter_date(cls, usage_data, start_date, end_date):
        filter_data = [i for i in usage_data if start_date <= i["date"] <= end_date]
        return cls(filter_data)
    

    # 정적 메서드
    @staticmethod
    def max_usage(usage_data):
        return max(usage_data, key = lambda x: x["usage"])
    
    def __str__(self):
        # 사용량 데이터를 보기 좋게 표현
        return f"전력 사용량 데이터: {self.usage_data}"
    
home = HomeElectricityData(electricity_usage)
home.calculate_total_usage()
print("총 전력 사용량", home.total_usage)
my_date = "2024-11-03"
print(f"{my_date}의 사용량: {home.get_usage_on_data(my_date)}")
end_date = "2024-11-05"
between_list = HomeElectricityData.filer_date(home.usage_data, my_date, end_date)
print("특정 날짜 범위 내의 사용량", between_list)
