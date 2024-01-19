# -*- coding: utf-8 -*-
"""Coding Assignment-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R-V516ZORpH-5ZvVjhhYEf1D0kI6q3i6

# **Kth Row of Pascal's Triangle**
"""

def getRow(rowIndex):
    if rowIndex < 0:
        return []
    row = [1]

    for i in range(1, rowIndex + 1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)

        row = new_row

    return row

k = int(input())
result = getRow(k)
print(result)

"""# **Stairs**"""

def climbStairs(A):
    if A <= 0:
        return 0
    if A == 1:
        return 1
    if A == 2:
        return 2
    dp = [0] * (A + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, A + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[A]


k=int(input("number of stairs"))
print("number of possibilities are: ",climbStairs(k))

"""# **Best Time to Buy and Sell Stocks**"""

def maxProfit(A):
    if not A or len(A) < 2:
        return 0
    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


print(maxProfit([1, 4, 5, 2, 4]))

"""# **Repeat and Missing Number Array**"""

def findDuplicates(nums):
    n = len(nums)
    for i in range(n):
        while nums[i] != i + 1:
            if nums[i] == nums[nums[i] - 1]:
                return [nums[i], i + 1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

k=int(input("enter the number of digits "))
p=[]
for i in range(k):
  a=int(input())
  p.append(a)
output_result = findDuplicates(p)
print(output_result)

"""# **Distribute Candy**"""

def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    total_candies = sum(candies)
    return total_candies

l=int(input("number of children "))
p=[]
for i in range(l):
  a=int(input("enter the rating "))
  p.append(a)
output_result = candy(p)
print(output_result)

