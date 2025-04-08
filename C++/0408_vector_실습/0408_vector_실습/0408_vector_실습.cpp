// 0408_vector_실습.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main()
{
	// 실습1. vector 조작하기

	// 1) Vector를 사용하여 정수를 저장하는 빈 벡터 선언
	//vector<int> intVector;
	//// 2) 사용자로부터 5개의 정수를 입력받아 벡터에 추가
	//for (int i = 0; i < 5; ++i) {
	//	int num;
	//	cout << "정수를 입력하세요: ";
	//	cin >> num;
	//	intVector.push_back(num);
	//}
	//// 3) 벡터의 모든 크기 출력
	//cout << "벡터의 크기: " << intVector.size() << endl;
	//// 4) 벡터의 모든 원소 출력
	//cout << "벡터의 원소: ";
	//for (int i = 0; i < intVector.size(); ++i) {
	//	cout << intVector[i] << " ";
	//}
	//cout << endl;
	//// 5) 가장 큰 값을 찾아 출력
	//int maxValue = intVector[0];
	//for (int i = 1; i < intVector.size(); ++i) {
	//	if (intVector[i] > maxValue) {
	//		maxValue = intVector[i];
	//	}
	//}
	//cout << "가장 큰 값: " << maxValue << endl;
	//// 6) 벡터의 모든 원소를 두배로
	//for (int i = 0; i < intVector.size(); ++i) {
	//	intVector[i] *= 2;
	//}
	//// 7) 인덱스를 입력받아 해당 인덱스에 있는 원소 제거
	//int indexToRemove;
	//cout << "제거할 인덱스를 입력하세요 (0~" << intVector.size() - 1 << "): ";
	//cin >> indexToRemove;
	//if (indexToRemove >= 0 && indexToRemove < intVector.size()) {
	//	intVector.erase(intVector.begin() + indexToRemove);
	//	cout << "인덱스 " << indexToRemove << "의 원소가 제거되었습니다." << endl;
	//}
	//else {
	//	cout << "잘못된 인덱스입니다." << endl;
	//}
	//// 8) 인덱스를 입력받아 해당 인덱스에 있는 새로운 원소 삽입
	//int indexToInsert;
	//int newValue;
	//cout << "삽입할 인덱스를 입력하세요 (0~" << intVector.size() << "): ";
	//cin >> indexToInsert;
	//if (indexToInsert >= 0 && indexToInsert <= intVector.size()) {
	//	cout << "삽입할 값을 입력하세요: ";
	//	cin >> newValue;
	//	intVector.insert(intVector.begin() + indexToInsert, newValue);
	//	cout << "인덱스 " << indexToInsert << "에 " << newValue << "가 삽입되었습니다." << endl;
	//}
	//else {
	//	cout << "잘못된 인덱스입니다." << endl;
	//}

	// 실습2. 2차원 행렬 만들기
	// 사용자가 입력한 행과 열 크기에 맞는 동적 2차원 배열을 생성하고, 각 요소를 (i+1)*(J+1) 값으로 초기화한 행렬을 출력하세요.
	//int rows, cols;
	//cout << "행의 크기를 입력하세요: ";
	//cin >> rows;
	//cout << "열의 크기를 입력하세요: ";
	//cin >> cols;
	//vector<vector<int>> matrix(rows, vector<int>(cols));
	//for (int i = 0; i < rows; ++i) {
	//	for (int j = 0; j < cols; ++j) {
	//		matrix[i][j] = (i + 1) * (j + 1);
	//	}
	//}
	//cout << "생성된 행렬:" << endl;
	//for (int i = 0; i < rows; ++i) {
	//	for (int j = 0; j < cols; ++j) {
	//		cout << matrix[i][j] << " ";
	//	}
	//	cout << endl;
	//}
	// 실습3. 2차원 행렬 만들기
	// 사용자가 입력한 행과 열, 행렬의 원소를 직접 입력하도록 구현하고 각 행과 열의 합을 구하도록 구현해보세요.
//	int rows, cols;
//
//	cout << "행의 개수를 입력하세요: ";
//	cin >> rows;
//	cout << "열의 개수를 입력하세요: ";
//	cin >> cols;
//
//	vector<vector<int>> matrix(rows, vector<int>(cols));
//	vector<int> rowSum(rows, 0);
//	vector<int> colSum(cols, 0);
//
//	cout << "행렬의 원소를 입력하세요:" << endl;
//	for (int i = 0; i < rows; ++i) {
//		for (int j = 0; j < cols; ++j) {
//			cin >> matrix[i][j];
//		}
//	}
//
//	cout << "행렬의 원소:" << endl;
//	for (int i = 0; i < rows; ++i) {
//		for (int j = 0; j < cols; ++j) {
//			cout << matrix[i][j] << " ";
//			rowSum[i] += matrix[i][j];
//			colSum[j] += matrix[i][j];
//		}
//		cout << endl;
//	}
//	cout << "행의 합:" << endl;
//	for (int i = 0; i < rows; ++i) {
//		cout << "행 " << i+1 << ": " << rowSum[i] << endl;
//	}
//	cout << "열의 합:" << endl;
//	for (int j = 0; j < cols; ++j) {
//		cout << "열 " << j+1 << ": " << colSum[j] << endl;
//	}
//
//	return 0;
// 
// 
// // 실습3. 다른 방법
	int rows, cols;
    
	cout << "행과 열의 수를 입력하세요: ";
	cin >> rows >> cols;

	int matrix[rows][cols];

	cout << "행렬 원소를 입력하세요:" << endl;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cin >> matrix[i][j];
		}
	}

	// 행의 합 계산
	cout << "각 행의 합:" << endl;
	for (int i = 0; i < rows; i++) {
		int rowSum = 0;
		for (int j = 0; j < cols; j++) {
			rowSum += matrix[i][j];
		}
		cout << "행 " << i + 1 << ": " << rowSum << endl;
	}

	// 열의 합 계산
	cout << "각 열의 합:" << endl;
	for (int j = 0; j < cols; j++) {
		int colSum = 0;
		for (int i = 0; i < rows; i++) {
			colSum += matrix[i][j];
		}
		cout << "열 " << j + 1 << ": " << colSum << endl;
	}
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
