from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_list = Counter(nums)
        for key in freq_list:
            freq = freq_list[key]
            if freq == 1:
                return key
        return None