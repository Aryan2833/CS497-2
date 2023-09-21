import random
def findKthLargest(nums, k):
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] > pivot:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    left, right = 0, len(nums) - 1

    while left <= right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k - 1:
            return nums[pivot_index]
        elif pivot_index > k - 1:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
result1 = findKthLargest(nums1, k1)
print(result1)

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
result2 = findKthLargest(nums2, k2)
print(result2)
