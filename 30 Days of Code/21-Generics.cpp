//Programmer : Jatin Sharma
//The option to Solving this problem is not available in python, So here in C++

#include <iostream>
#include <vector>
#include <string>

using namespace std;
//***************************************************

template<typename T>void printArray(vector<T> n){
    for(T i: n)
        cout << i << endl;
}

//***********************************************

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
