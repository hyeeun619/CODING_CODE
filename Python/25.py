# 실습 건상상태 클래스

# (메서드)
# 1. name -> getter, setter
# 2. hp -> getter, setter
# 3. exercise(시간) (운동하면 체력 1증가)
# 4. drink(잔) (술마시면 체력 1감소)
# 5. info() - 이름, hp 출력

class Health:
    def __init__(self, name):
        self._name = name # 인스턴스의 이름
        self._hp = 100 # 체력(health point) : 초기값 100

    def get_name(self):
        return self._name
        
    def set_name(self, name):
        self._name = name
    
    def get_hp(self):
        return self._hp
    
    def set_hp(self, value): # hp 범위 1~100
        #  1보다 작은 값이 들어오면 1
        # 100보다 큰 값이 들어오면 100
        if value > 100:
            self._hp = 100
        elif value < 1:
            self._hp = 1
        else: # 정상적인 범위의 값값
            self._hp = value

    def excrcise(self, hour):
        # hour 만큼 hp 값 증가
        self.set_hp(self._hp + hour)
        # 얼마나 운동했는지 정보 출력
        print(f"{hour}시간 운동하다.")

    def drink(self, cups):
        # cups 만큼 hp 값 감소
        self.set_hp(self._hp - cups)
        # 얼마나 마셨는지 정보 출력
        print(f"술을 {cups}잔 마셨다.")

    def info(self):
        print(f"{self.get_name()} 님의 hp는 {self.get_hp()} 입니다.")

p1 = Health("나몸짱")
p1.set_hp(80)
p1.excrcise(4)
p1.drink(2)
p1.info()

p2 = Health("나약해")
p2.set_hp(30)
p2.excrcise(1)
p2.drink(10)
p2.info()
