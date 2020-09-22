// Programmer : Jatin Sharma

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;

    cin >> a >> b >> c >> d >> e;

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << fixed << setprecision(2) << d << endl;
    cout << fixed << setprecision(5) << e << endl;
    return 0;
}
