# Date - Oct 5, 2020 By Jatin Sharma


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    '''for i in range(0,d,1):
        temp = a[0]
        for j in range(0,n-1,1):
            a[j] = a[j+1]
        a[n-1] = temp

    for x in range(n):
        print(a[x] , end = " ")'''
    for y in range(d, n, 1):
        print(a[y], end=' ')
    for z in range(0, d, 1):
        print(a[z], end=' ')
