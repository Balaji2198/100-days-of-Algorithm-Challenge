'''
Input Format:
The first line contains 3 space-separated integers, n, k, and q, respectively. 
The second line contains n space-separated integers, where each integer i describes array element a[i]. 
Each of the q subsequent lines contains a single integer denoting m.


Output Format:
For each query, print the value of the element at index m of the rotated array on a new line.

'''



from collections import deque


n,k,q = map(int, raw_input().strip().split(' '))
a = deque(map(int,raw_input().strip().split(' ')))
a.rotate(k)
for i in range(q):
    print a[(int(raw_input()))]