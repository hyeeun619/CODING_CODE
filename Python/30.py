# 추상화
# 추상클래스와 추상메서드

# abd 모듈 불러오기
from abc import ABC, abstractmethod

# 추상 클래스 정의
class PaymentSystem(ABC): # P.S 클래스는 ABC를 상속받는 추상 클래스
    # 추상 메서드 2개 정의
    # : P.S 클래스에서 구현하지 않고, 해당 클래스를 상속받는 자식 클래스에서 "반드시 구현"
    @abstractmethod
    def authenticate(self): # 인증 처리
        pass

    @abstractmethod
    def process_payment(self, amount): # 결제 처리
        pass

    # 일반 메서드
    def payment_info(self, amount): # 결제 완료 후 정보 출력
        print(f"{amount}원 결제 완료!")

# 자식클래스 정의 - 카카오페이
class KaKaoPay(PaymentSystem):
    # 추성메서드 구현
    def authenticate(self):
        print("[인증완료] 카카오페이")

    def process_payment(self, amount):
        print(f"[결제진행]카카오페이 {amount}원")

# 자식클래스 정의 - 네이버페이
class NaverPay(PaymentSystem):
        # 추성메서드 구현
    def authenticate(self):
        print("[인증완료] 네이버페이")

    def process_payment(self, amount):
        print(f"[결제진행]네이버페이 {amount}원")

    # NaverPay 클래스에서만 사용하는 일반메서드
    def discount(self, amount):
        discount_amount = amount * 0.05 # 5% 할인
        print(f"[이벤트] 네이버페이 5% 이벤트 적용으로 {discount_amount}원 할인")
        return amount - discount_amount # 정가 - 할인액 = 구매액


pay = 3600
kakao = KaKaoPay()
kakao.authenticate()
kakao.process_payment(pay)
kakao.payment_info(pay)

# 추상클래스 인스턴스 불가!
# test = PaymentSystem()
# test.authenticate()
# TypeError: Can't instantiate abstract class PaymentSystem without an implementation for abstract methods 'authenticate', 'process_payment'

naver = NaverPay()
naver.authenticate()
pay_after_discount = naver.discount(pay)
print(f"할인 후 결제액: {pay_after_discount}")