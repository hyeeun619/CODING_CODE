// 0408.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

bool isCheck(string s) {
	for (char c : s) {
		if (!isdigit(c)) {
			return false;
		}
	}
	return true;
}

int main()
{
	string s1 = "Hello ";
	string s2 = "World!";

	cout << s1 + s2 << endl;
	cout << (s1 < s2) << endl;

	//string sentence;
	//cout << "문장을 입력하세요: ";
	//getline(cin, sentence);
	//cout << "당신이 입력한 문장은: " << sentence << endl;

	// string 함수
	cout << "s1.at(2) : " << s1.at(2) << endl;
	cout << "s2.at(2) : " << s2.at(2) << endl;

	cout << "s1[4] : " << s1[4] << endl;
	cout << "s2[4] : " << s2[4] << endl;

	cout << "s1.front() : " << s1.front() << endl;
	cout << "s1.back() : " << s1.back() << endl;

	cout << "s2.front() : " << s2.front() << endl;
	cout << "s2.back() : " << s2.back() << endl;

	cout << "s1.length() : " << s1.length() << endl;
	cout << "s1.size() : " << s1.size() << endl;

	s1.resize(10);
	cout << "s1.resize(10) : " << s1 << endl;;
	cout << "s1.length() : " << s1.length() << endl;

	s1.resize(11, 'a');
	cout << "s1.resize(11 , 'a') : " << s1 << endl;
	cout << "s1.length() : " << s1.length() << endl;

	string s3 = "hello! ";
	string s4 = "world!";
	//cout << "s3.empty() : " << s3.empty() << endl;

	//s3.append(s4);
	//cout << "s3.append(s4) : " << s3 << endl;

	//s3.append(s4, 1, 3);
	//cout << "s3.append(s4, 3, 4) : " << s3 << endl;

	//s3.insert(1, s4);
	//cout << "s3.insert(1, s4) : " << s3 << endl;

	//s3.replace(2,1, s4);
	//cout << "s3.replace(1,3, s4) : " << s3 << endl;

	//s3.clear();
	//cout << "s3.clear() : " << s3 << endl;

	//s3.erase(1, 2);
	//cout << "s3.erase(1, 2) : " << s3 << endl;


	s3 += s4;
	cout << "s3 :" << s3 << endl;

	string s5 = "!!";
	cout << "s3.find(!) : " << s3.find(s5) << endl;
	cout << "s3.find(!, 6) : " << s3.find(s5, 6) << endl;

	size_t pos = s3.find(s5);
	// 문자열을 찾으면 실행
	// 못찾으면 npos와 같이 동일
	if (pos != string::npos) {
		cout << "찾은 문자열 첫 인덱스: " << pos << endl;
	}

	cout << "s3.substr(3) :" << s3.substr(3) << endl;
	cout << "s3.substr(3, 3) :" << s3.substr(3, 3) << endl;

	string s6 = "aaa";
	string s7 = "ccc";
	cout << "s6.compare(s7) :" << s6.compare(s7) << endl;

	cout << "isdigit('5') :" << isdigit('5') << endl;
	cout << "isdigit('a') :" << isdigit('a') << endl;

	cout << "isalpha('3') :" << isalpha('3') << endl;
	cout << "isalpha('a') :" << isalpha('a') << endl;

	cout << "toupper('a') :" << char(toupper('a')) << endl;
	cout << "toupper('C') :" << char(toupper('C')) << endl;

	cout << "tolower('C') :" << char(tolower('C')) << endl;
	cout << "tolower('b') :" << char(tolower('b')) << endl;

	cout << "stoi('19') :" << typeid(stoi("19")).name() << endl;
	cout << "stof('19.23') :" << typeid(stof("19.23")).name() << endl;

	cout << "to_string(19.23) :" << typeid(to_string(19.23)).name() << endl;


	//실습1. string 사용해보기
   /*string s = "Police say two people are suspected of trying to create a shortcut for their construction work.The two have been detained and the case is under further investigation.The 38 - year - old man and 55 - year - old woman were working near the affected area, the 32nd Great Wall.";

   cout << "s의 문자열의 길이: " << s.length() << endl;
   cout << "s의 100번째 문자: " << s[99] << endl;
   cout << "s의 \"two\"라는 문자가 처음 나오는 index: " << s.find("two") << endl;
   cout << "s의 \"two\"라는 문자가 두번째 나오는 index: " << s.find("two", s.find("two") + 1) << endl;*/

   // 실습2. string 사용해보기
   //string s = "Codingon";
   //
   //s[0] = 'c';
   //cout << s << endl;
   //// "ding"이라는 부분 문자열 반환
   //cout << s.substr(2, 4) << endl;
   //// "coooooon"이 되도록 변경
   //s.replace(1, 7, "oooooon");
   //cout << s << endl;
   ////"con"이 되도록 변경
   //s.replace(1, 7, "on");
   //cout << s << endl;

   //실습3. string 사용해보기
   //int num1, num2;
   //string str1, str2;
   //while (true) {
   //	cout << "첫 번째 숫자를 입력하세요: ";
   //	cin >> str1;
   //	cout << "두 번째 숫자를 입력하세요: ";
   //	cin >> str2;
   //	if (isdigit(str1[0]) && isdigit(str2[0])) {
   //		num1 = stoi(str1);
   //		num2 = stoi(str2);
   //		cout << "두 숫자를 이어 붙인 값: " << str1 + str2 << endl;
   //		cout << "두 숫자의 합: " << num1 + num2 << endl;
   //		break;
   //	}
   //	else {
   //		cout << "숫자가 아닙니다." << endl;
   //	}
   //}
}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
