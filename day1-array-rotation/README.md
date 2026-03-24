# Day 1: Array Rotation

## Problem
Implement a function that rotates an array k steps to the right in-place with O(1) extra space.

## Requirements
- Modify the array in-place (no extra space proportional to input size)
- Handle cases where k > n (use modulo operation)
- Handle edge cases: empty array, single element, k = 0

## Example
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

## Hints
- Think about reversing portions of the array
- Consider the relationship between array indices and rotation
- What happens when you reverse the entire array first?

## Files
- `array_rotation.py`: Problem setup with function stub and test cases

## Interview Relevance
This problem tests your understanding of:
- In-place array manipulation
- Space complexity optimization
- Handling edge cases in algorithms
- Mathematical relationships in array operations

Implement your solution and discuss your approach!