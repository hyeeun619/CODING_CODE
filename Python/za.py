vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '이프로']

# 조건1. 사용자는 소비자, 주인 두 가지 종류로 입력받기 (번호 또는 값 입력), 그 외의 값은 잘못된 값으로 출력력
while True:
    sa = input("사용자 종류를 입력하세요:\n1. 소비자 \n2. 주인")
    if sa == "1" or sa == "소비자":
        drink= input("마시고 싶은 음료는 무엇인가요?")
        if drink in vending_machine : 
            print(f"{drink}를 드릴게요.")
            vending_machine.remove(drink)
            print(f"남은 음료수 : {vending_machine}")
        else:
            print("해당 음료는 없습니다.")
    elif sa == "2" or sa == "주인":
        ha = input("할 일 선택 \n1. 추가 \n2. 삭제")
        if ha == "1" or ha == "추가":
            drink = input("추가할 음료수?")
            vending_machine.add(drink)
            print("추가완료")
            print(f"남은 음료수 : {vending_machine}")
        if ha == "2" or ha == "삭제":
            drink = input("삭제할 음료수?")
            if drink in vending_machine :
                vending_machine.remove(drink)
                print("삭제 완료")
                print(f"남은 음료수 : {vending_machine}")
            else:
                print(f"{drink}는 지금 없네요")
    else:
        print("존재하지 않습니다.")


# 자판기 프로그램 과제 다른방법



# check_machine() : 남은 음료수를 확인할 수 있는 함수
def check_machine():
    return vending_machine
print(f"남은 음료수 : {vending_machine}")


# is_drink() : 음료수가 있는지 확인하는 함수
def is_drink(drink):
    if is_drink in vending_machine:
        return (f"{drink} 있습니다.")
    else:
        return (f"{drink} 없습니다.")
    
# add_drink : 음료수를 추가하는 함수
def add_drink(drink):
    vending_machine.append(drink)
    return(f"{drink} 추가완료") 

# remove_drink : 음료수를 제거하는 함수
def remove_drink(drink):
    vending_machine