#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void vectorShow(vector<int> v) {
    for (int i = 0; i < v.end() - v.begin(); i++) {
        cout << v[i] << ", ";
    }
    cout << endl;
}


int main()
{
    // 빈 벡터 선언
    vector<int> v1;
    vector<int> v2(5, 10);
    vector<int> v3 = { 1,2,3,4,5 };

    cout << "v2.at(2) : " << v2.at(2) << endl;
    cout << "v3[2] : " << v3[2] << endl;

    cout << "v3.front() : " << v3.front() << endl;
    cout << "v3.back() : " << v3.back() << endl;

    for (int i = 0; i < v3.end() - v3.begin(); i++) {
        cout << v3[i] << ", ";
    }
    cout << endl;
    cout << "v3.end() - v3.begin() : " << v3.end() - v3.begin() << endl;
    cout << "v3.begin()의 역참조 : " << *(v3.begin() + 1) << endl;

    v3.push_back(6);
    cout << "v3.push_back(6) :";
    vectorShow(v3);

    v3.pop_back();
    cout << "v3.pop_back() :";
    vectorShow(v3);

    v3.insert(v3.begin() + 3, 3);
    cout << "v3.insert(v3.begin() + 3, 3) :";
    vectorShow(v3);

    v3.erase(v3.end() - 2);
    cout << "v3.erase(v3.end() - 2) :";
    vectorShow(v3);

    vector<int> v4 = { 3, 3,1,5,2,4 };
    cout << "v4 :";
    vectorShow(v4);

    reverse(v4.begin(), v4.end());
    cout << "reverse(v4.begin(), v4.end()) :";
    vectorShow(v4);

    sort(v4.begin(), v4.end());
    cout << "sort(v4.begin(), v4.end()) :";
    vectorShow(v4);
    reverse(v4.begin(), v4.end());
    cout << "reverse(v4.begin(), v4.end()) :";
    vectorShow(v4);

    auto it = find(v4.begin(), v4.end(), 3);
    cout << "it - v4.begin() :" << it - v4.begin() << endl;

    auto count1 = count(v4.begin(), v4.end(), 3);
    cout << "count(v4.begin(), v4.end(), 3) :" << count1 << endl;


    vector<vector<int>> matrix(3, vector<int>(3, 0));
    cout << "matrix[1][1] :" << matrix[1][1] << endl;
    //{ 
    //    { 0, 0, 0 },
    //    { 0,0,0 },
    //    { 0,0,0 },
    //}