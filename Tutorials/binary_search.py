from random import randint


def binary_search(nums, target):
    low = 0
    high = len(nums)
    while low <= high:
        mid = (high + low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return (mid, nums[mid])
    return False


if __name__ == "__main__":
    target = randint(0, 100)
    nums = [x for x in range(100)]

    for _ in range(30):
        rem = randint(0, 100)
        if rem in nums:
            nums.remove(rem)

    print(f"Searching For: {target}")
    result = binary_search(nums, target)
    print(result)
