# def canBeIncreasing(nums):
#     a = 0
#     for i in range(1, len(nums) - 1):
#         if nums[i - 1] < nums[i + 1] < nums[i]:
#             a += 1
#         elif a == 0 and nums[i - 1] < nums[i] < nums[i + 1]:
#             return True
#     return a % 2 == 1
#
#
# print(canBeIncreasing([1,2,10,5,7]))


def canBeIncreasing(nums):
    f = False
    a = nums[0] -1
    for i in nums:
        print(f, a, i)
        if a > i:
            if f:
                return False
            f = True
        a = i
    return True


print(canBeIncreasing([2,3,1,2]))
