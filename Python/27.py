# 상속
# 부모클래스가 생성자가 없을 때
# -> 자식클래스에서 부모클래스 생성자를 호출 할 필요 x

class Animal:
    #  생성자 없음

    # 두 개의 메서드 정의
    def speak(self):
        print("동물 소리를 낸다")

    def move(self):
        print("동물이 움직인다")

class Cat(Animal):
    #  Animal 클래스 상속 (Animal의 속성, 메서드 사용)
    def meow(self):
        print("야옹!")

cat = Cat()
cat.meow() # Cat 클래스의 meow() 메서드 호출
cat.speak() # Animal 클래스의 speak() 메서드 호출
cat.move() # Animal 클래스의 move() 메서드 호출

# 부모클래스의 생성자가 존재할 때
# -> 자식클래스의 생성자에서 super().__init__()으로 부모클래스 생성자를 명시적으로 호출
class Animal:
    #  name 속성
    def __init__(self, name):
        self.name = name

    #  메서드 2개
    def speak(self):
        print(f"{self.name}가 소리를 냅니다")

    def move(self):
        print(f"{self.name}가 움직입니다")

# 자식클래스
class Cat(Animal):
    def __init__(self, name, sound = "냐옹"):
        super().__init__(name) # 부모클래스 생성자 호출
        # -> name 속성은 부모클래스에 전달해 name을 설정
        self.sound = sound # 자식클래스에서 sound를 속성 설정

    # 메서드 1개
    def meow(self):
        print(f"{self.name}가 {self.sound} 짖습니다")


cat = Cat("장화", "캬아악")
cat.meow()
cat.move()
cat.speak()

cat2 = Cat("나비")
cat2.meow()
cat2.move()
cat2.speak()