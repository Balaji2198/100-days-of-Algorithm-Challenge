'''
The Utopian Tree goes through 2 cycles of growth every year.
Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after n growth cycles?

Input Format:
The first line contains an integer, t, the number of test cases. 
t subsequent lines each contain an integer, n, denoting the number of cycles for that test case.

Output Format:
For each test case, print the height of the Utopian Tree after n cycles. Each height must be printed on a new line
'''

for f in range(int(raw_input())):
    h = 1
    n = int(raw_input())
    for i in range(1, n+1):
        if i%2 == 0:
            h += 1;
        else:
            h *= 2;
    print h