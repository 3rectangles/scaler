"""
Problem Description
Given an array of size N, find the subarray of size K with the least average.



Problem Constraints
1<=k<=N<=1e5
-1e5<=A[i]<=1e5


Input Format
First argument contains an array A of integers of size N.
Second argument contains integer k.


Output Format
Return the index of the first element of the subarray of size k that has least average.
Array indexing starts from 0.


Example Input
Input 1:
A=[3, 7, 90, 20, 10, 50, 40]
B=3
Input 2:

A=[3, 7, 5, 20, -10, 0, 12]
B=2


Example Output
Output 1:
3
Output 2:

4


Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:

 Subarray between [4, 5] has minimum average
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ksum = 0
        for i in range(B):
            ksum += A[i]
        res = ksum
        idx = 0
        for i in range(1, len(A) - B + 1):
            ksum = ksum - A[i - 1] + A[i + B - 1]
            if ksum < res:
                res = ksum
                idx = i
        
        return idx