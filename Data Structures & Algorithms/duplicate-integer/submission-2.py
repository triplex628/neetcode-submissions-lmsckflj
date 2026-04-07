class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        min_val = min(nums)
        max_val = max(nums)

        offset = -min_val  # сдвиг
        arr = [0] * (max_val - min_val + 1)

        for x in nums:
            idx = x + offset
            if arr[idx] == 1:
                return True
            arr[idx] = 1

        return False