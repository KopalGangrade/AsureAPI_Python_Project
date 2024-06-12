# You are given an array of integers. Print an array where each index has the sum of all numbers in the original array except the number at that index.
# Sample Input
# 7 3 6 7 5

# Sample Output
# 21 25 22 21 23


# A=list(map(int,input().split()))
# i=0
# while i<len(A):
#     sum=0                                                                 
#     j=0
#     while j<len(A):
#         if (i!=j):
#             sum+=A[j] 
#         j+=1
#     i+=1
#     print(sum)


# ------------------------------------------------------------

# 7 3 6 7 5

# A=list(map(int,input().split()))
# b=0
# i=0
# sum=0
# while i < len(A):
#     if (i!=b):
#         sum+=A[i]
#     i+=1
# print(sum)


# A=list(map(int,input().split()))
# i=0 
# j=0
# sum=0
# while i<len(A) and j<len(A):
#     if (i!=j):


#     if (i!=b):
#         sum+=A[i]
#     b+=1
# print(sum)
# i+=1



A=list(map(int,input().split()))
sum=0
i=0
while i < len(A):
    sum+=A[i]
    i+=1

m=sum
j=0
while j < len(A):
    sum1=0
    sum1 = m-A[j] #28-7
    j+=1
    print(sum1)










      
    
