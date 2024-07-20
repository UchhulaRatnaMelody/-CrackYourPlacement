#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        if (M==0 or N==0):
            return 0
        A.sort()
        if N < M:
            return -1
        min_diff = A[N-1] - A[0]
        for i in range(len(A)-M+1):
            min_diff = min(min_diff,A[i+M-1]-A[i])
        return min_diff

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends