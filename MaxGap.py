def maximumGap(nums):
    if len(nums) < 2:
        return 0

    max_val, min_val = max(nums), min(nums)

    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))

    num_buckets = (max_val - min_val) // bucket_size + 1

    buckets = [[] for _ in range(num_buckets)]

    for num in nums:
        index = (num - min_val) // bucket_size
        if not buckets[index]:
            buckets[index] = [num, num]
        else:
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

    max_gap = 0
    prev_max = min_val

    for i in range(num_buckets):
        if not buckets[i]:
            continue
        curr_min, curr_max = buckets[i]
        max_gap = max(max_gap, curr_min - prev_max)
        prev_max = curr_max

    return max_gap


nums1 = [3, 6, 9, 1]
result1 = maximumGap(nums1)
print(result1)

nums2 = [10]
result2 = maximumGap(nums2)
print(result2)
