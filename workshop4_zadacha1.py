nums = [10, 9, 2, 5, 3, 7, 101, 18, 1]

def length(nums):
    N = len(nums)
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(length(nums))