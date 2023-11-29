def search_insert(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            low = mid + 1  # Adjust low pointer
        else:
            high = mid - 1  # Adjust high pointer

    return low  # Return the index for insertion position

nums = [1,3,5,7]
target = 2
# Expected answer = 1
# Since 2 would get inserted at index 1 in this sorted list
search_insert(nums, target)