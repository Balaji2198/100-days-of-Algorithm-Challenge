
'''
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison scores by comparing a0 with b0, a1 with b1 and a2 with b2.

If ai > bi, then Alice is awarded  point.
If bi > ai, then Bob is awarded  point.
If ai = bi, then neither person receives a point.
Given A and B, can you compare the two challenges and print their respective comparison points?


Input Format:

The first line contains 3 space-separated integers, a0, a1, and a2, describing the respective values in triplet. 
The second line contains 3 space-separated integers, b0, b1, and b2, describing the respective values in triplet.


Output Format:

Print two space-separated integers denoting the respective comparison scores earned by Alice and Bob.
'''


a = map(int, raw_input().split())
b = map(int, raw_input().split())
ap = 0
bp = 0
for i, j in zip(a, b):
    if i>j:
        ap += 1
    elif j>i:
        bp += 1
print ap, bp