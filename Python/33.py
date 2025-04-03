# 총정리
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 대체 생성자 패턴턴
    @classmethod
    def from_string(cls, date_string):
        """
        문자열로부터 Date 객체를 생성하는 클래스 메서드
        ex. '2025-01-13' -> Date(2025, 01, 13)
        date = "2025-01-13"
        print(date.split("-"))  # ['2025', '01', '13']
        phone_number = "010-1234-4321"
        print(phone_number.split("-"))  # ['010', '1234', '4321']
        """
        # map(int, ['2025', '01', '13'])
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day) # Date(year, month, day)
    
    @staticmethod
    def is_valid_date(date_string):
        """
        유효한 날짜를 입력했는지를 검증 "2025-13-99"
        """
        # 1. 문자열 분리
        parts = date_string.split("-") # ["2025", "13", "99"]

        # 2. 각 부분을 숫자로 변환
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        # 3. 월과 일의 범위 검사
        if month < 1 or month > 12:
            return False
        
        if day < 1 or day > 31:
            return False
        
        return True
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
    
# 사용
dt1 = Date(2025, 1, 13)
dt2 = Date.from_string("2025-01-14")
is_valid = Date.is_valid_date("2025-01-14")
is_valid2 = Date.is_valid_date("2025-01-99")
print(dt1)
print(dt2)
print(is_valid)
print(is_valid2)

# 클래스 메서드 vs. 정적 메서드
# "목적에 따라서 논리적으로 개발자가 구별해서 쓰면 됨"
# -> "기술적인 차이보다 목적에 따라 구분해서 사용하는 것이 중요"
