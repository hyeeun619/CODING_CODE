# 자판기 프로그램 함수화

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '이프로']


# check_machine() : 남은 음료수를 확인할 수 있는 함수
def check_machine():
    print("남은 음료수: ", vending_machine)

def  is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    vending_machine.append(drink)
    print(f"{drink} 추가 완료")

def remove_drink(drink):
    if is_drink(drink):
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요")

'''
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
'''