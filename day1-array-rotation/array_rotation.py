"""
Day 1: Array Manipulation
Concept: Efficient array operations and in-place modifications - essential for optimizing space complexity in interviews
Problem: Implement a function that rotates an array k steps to the right in-place with O(1) extra space
Language: Python
"""

def rotate_array(nums, k):
    """
    Rotate the array to the right by k steps in-place with O(1) extra space.

    Args:
        nums: List[int] - the array to rotate
        k: int - number of steps to rotate right

    Returns:
        None (modify nums in-place)
    """
    # TODO: Implement your solution here

    def reverse_nums(nums, start=0, end=None):
        left = start
        right = end if not end is None else len(nums) - 1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    if len(nums) < 2:
        return
    
    k %= len(nums)
    if k == 0:
        return

    reverse_nums(nums)
    reverse_nums(nums, start=k)
    reverse_nums(nums, end=(k-1))

    return

# Test cases - run these to verify your solution
if __name__ == "__main__":
    # Test case 1: Basic rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(nums1, 3)
    print("Test 1 - Rotate [1,2,3,4,5,6,7] by 3:", nums1)
    # Expected: [5, 6, 7, 1, 2, 3, 4]

    # Test case 2: k = 0 (no rotation)
    nums2 = [1, 2, 3]
    rotate_array(nums2, 0)
    print("Test 2 - Rotate [1,2,3] by 0:", nums2)
    # Expected: [1, 2, 3]

    # Test case 3: k > n
    nums3 = [1, 2, 3, 4]
    rotate_array(nums3, 5)  # 5 % 4 = 1
    print("Test 3 - Rotate [1,2,3,4] by 5:", nums3)
    # Expected: [4, 1, 2, 3]

    # Test case 4: Single element
    nums4 = [1]
    rotate_array(nums4, 1)
    print("Test 4 - Rotate [1] by 1:", nums4)
    # Expected: [1]

    # Test case 5: Empty array
    nums5 = []
    rotate_array(nums5, 3)
    print("Test 5 - Rotate [] by 3:", nums5)
    # Expected: []

    print("Check your results against the expected outputs above!")