from typing import List, Tuple

class TwoSum:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
        # initialize an empty dictionary to help map items in nums
        index_map = {}

        for i, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], i
            index_map[num] = i
