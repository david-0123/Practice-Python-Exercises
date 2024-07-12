import math

def binarySearch(nums, target):
    if len(nums) == 0:
        return False

    left = 0
    right = len(nums) - 1
    mid = math.ceil((left+right)/2)

    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binarySearch(nums[mid+1:], target)
    elif nums[mid] > target:
        return binarySearch(nums[:mid], target)

myList = [1,2,3,4,5,6]
print(binarySearch(myList, 0))