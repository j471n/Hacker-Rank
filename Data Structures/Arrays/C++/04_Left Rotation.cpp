// Date - Oct 5, 2020 By Jatin Sharma

#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int a[n];
    
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int j = k % n;
    
    for (int i = j; i < n; i++)
        cout << a[i] << " ";
    
    for (int i = 0; i < j; i++)
        cout << a[i] << " ";
    return 0;
}
