// Date - Oct 5, 2020 By Jatin Sharma

#include <iostream>
using namespace std;

int main()
{
    long int j, i, N, M, a, b, k, max = 0;
    cin >> N >> M;
    long int *ar = new long int[N]();
    for (i = 0; i < M; i++)
    {
        cin >> a >> b >> k;
        ar[a - 1] = ar[a - 1] + k;
        if (b < N)
        {
            ar[b] = ar[b] - k;
        }
    }
    k = 0;
    for (i = 0; i < N; i++)
    {
        k = k + ar[i];
        if (k > max)
        {
            max = k;
        }
    }
    cout << max << endl;
    return 0;
}