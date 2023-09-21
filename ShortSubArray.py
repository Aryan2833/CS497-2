from collections import deque

def shortestSubarrayWithSum(nums, k):
    n = len(nums)
    min_length = float('inf')

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    dq = deque()

    for i in range(n + 1):
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            min_length = min(min_length, i - dq.popleft())

        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()

        dq.append(i)

    return min_length if min_length != float('inf') else -1


nums1 = [1]
k1 = 1
result1 = shortestSubarrayWithSum(nums1, k1)
print(result1)

nums2 = [1, 2]
k2 = 4
result2 = shortestSubarrayWithSum(nums2, k2)
print(result2)

nums3 = [2, -1, 2]
k3 = 3
result3 = shortestSubarrayWithSum(nums3, k3)
print(result3)
