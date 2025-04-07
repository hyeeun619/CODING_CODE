// ConsoleApplication1.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//


#include <iostream>

using namespace std;

// 실습 1 동적 2차원 배열 생성 및 해제
//int main() {
//	int row = 3, cols = 3;
//	int** matrix = new int* [row];
//
//	for (int i = 0; i < row; i++) {
//		matrix[i] = new int[cols];
//	}
//
//	for (int i = 0; i < row; i++) {
//		for (int j = 0; j < cols; j++) {
//			matrix[i][j] = (i + 1) * (j + 1);
//		}
//	}
//
//	for (int i = 0; i < row; i++) {
//		for (int j = 0; j < cols; j++) {
//			cout << matrix[i][j];
//		}
//		cout << endl;
//	}
//
//	for (int i = 0; i < row; i++) {
//		delete[] matrix[i];
//	}
//	delete[] matrix;
//
//	return 0;
//}


// 실습 2 함수 포인터를 사용한 계산기
//int add(int a, int b) {
//	return a + b;
//}
//int subtract(int a, int b) {
//	return a - b;
//}
//int multiply(int a, int b) {
//	return a * b;
//}
//int divide(int a, int b) {
//	if (b == 0) {
//		cout << "0으로 나눌 수 없습니다." << endl;
//		return 0;
//	}
//		return a / b;
//}
//int main() {
//	int num1, num2;
//	char op;
//	int (*operation)(int, int);
//
//	cout << "숫자 두 개를 입력하세요. : ";
//	cin >> num1 >> num2;
//	cout << "연산자를 입력하세요 (+, -, *, /) : ";
//	cin >> op;
//
//	switch (op) {
//	case '+':
//		operation = add;
//		break;
//	case '-':
//		operation = subtract;
//		break;
//	case '*':
//		operation = multiply;
//		break;
//	case '/':
//		operation = divide;
//		break;
//	default:
//		cout << "잘못된 연산자입니다." << endl;
//		return 1;
//	}
//	int result = operation(num1, num2);
//	cout << "결과: " << result << endl;
//	return 0;
//}

// 실습1 포인터 기본 사용
//int main() {
//	int a = 10;
//	int* p = &a;
//
//	cout << "a의 값: " << a << endl;
//	cout << "*p의 값: " << *p << endl;
//	cout << "a의 주소: " << &a << endl;
//	cout << "p의 값: " << p << endl;
//
//	return 0;
//}

// 실습2 포인터를 이용한 값 변경
//int main() {
//	int a = 10;
//	int* p = &a;
//	cout << "a의 값: " << a << endl;
//	*p = 15;
//	cout << "포인터로 증가시킨 후 a의 값: " << a << endl;
//	return 0;
//}

// 실습3 포인터와 함수
//void swap(int* a, int* b) {
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
//int main() {
//	int a = 3, b = 7;
//	cout << "a: " << a << ", b: " << b << endl;
//	swap(&a, &b);
//	cout << "스왑 후 a: " << a << ", b: " << b << endl;
//	return 0;
//}

// 실습4 배열과 포인터
//int main() {
//	int arr[5] = { 10, 20, 30, 40, 50 };
//	int* p = arr;
//	cout << "배열의 첫 번째 요소: " << *p << endl;
//	cout << "배열의 두 번째 요소: " << *(p + 1) << endl;
//	cout << "배열의 세 번째 요소: " << *(p + 2) << endl;
//	cout << "배열의 네 번째 요소: " << *(p + 3) << endl;
//	cout << "배열의 다섯 번째 요소: " << *(p + 4) << endl;
//}

// 실습5 const 포인터 vs 포인터 to const
//int main() {
//	int a = 10, b = 20;
//	const int* p1 = &a;
//	int* const p2 = &a;
//}
// *p1 = 30;는 가능한가? -> 불가능, 이유 : p1은 const int형 포인터이므로, p1이 가리키는 값은 변경할 수 없다.
// p1 = &b;는 가능한가? -> 가능, 이유 : p1은 const int형 포인터이므로, p1이 가리키는 주소는 변경할 수 있다.
// *p2 = 30;는 가능한가? -> 가능, 이유 : p2는 int형 포인터이므로, p2가 가리키는 값은 변경할 수 있다.
// p2 = &b;는 가능한가? -> 불가능, 이유 : p2는 int형 포인터이므로, p2가 가리키는 주소는 변경할 수 없다.

// 실습6 이중 포인터
//int main() {
//	int a = 5;
//	int* p1 = &a;
//	int** p2 = &p1;
//	cout << "a의 값: " << a << endl; 
//	cout << "p1이 가리키는 값: " << *p1 << endl; 
//	cout << "p2가 가리키는 값: " << **p2 << endl; 
//	**p2 = 10;
//	cout << "a의 값: " << a << endl; 
//	cout << "p1이 가리키는 값: " << *p1 << endl; 
//	cout << "p2가 가리키는 값: " << **p2 << endl; 
//	return 0;
//}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
