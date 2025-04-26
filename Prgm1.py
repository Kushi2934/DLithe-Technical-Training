def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])
    return b
# Example:
val = [6, 7, 1, 3, 8, 2, 5]
max_value = rob(val)
print(f"Max stolen value: {max_value}")