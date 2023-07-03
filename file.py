def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = quick_sort(numbers)
print("Отсортированный список чисел:", sorted_numbers)
