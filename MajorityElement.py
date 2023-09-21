#Assignment 2 First Problem
def majority_element(nums):
    majority = nums[0]
    count = 1

    for n in nums[1:]:
        if count == 0:
            majority = n
            count = 1
        elif majority == nums:
            count += 1
        else:
            count -= 1
    return majority
nums = [3,2,3]
result = majority_element(nums)
print(result)