#1
def manual_isalnum(s):
    for char in s:
        if not (char.isalnum()):
            return False
    return True

#2
def manual_startswith(s, prefix):
    return s[:len(prefix)] == prefix


#3
def manual_endswith(s, suffix):
    return s[-len(suffix):] == suffix


#4
def manual_round(number, ndigits=0):
    if ndigits == 0:
        return int(number + 0.5) if number > 0 else int(number - 0.5)
    else:
        factor = 10 ** ndigits
        return int(number * factor + 0.5) / factor if number > 0 else int(number * factor - 0.5) / factor


#5
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        raise ValueError("Input arrays are not sorted")


#6
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0 

        return [1] + digits



#7
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        min_val, max_val = min(nums), max(nums)
        bucket_size = math.ceil((max_val - min_val) / (len(nums) - 1))
        buckets = [[float('inf'), float('-inf')] for _ in range((max_val - min_val) // bucket_size + 1)]
        
        for num in nums:
            if num == min_val or num == max_val: continue
            idx = (num - min_val) // bucket_size
            buckets[idx][0], buckets[idx][1] = min(buckets[idx][0], num), max(buckets[idx][1], num)
        
        max_gap, prev_max = 0, min_val
        for low, high in buckets:
            if low == float('inf'): continue
            max_gap = max(max_gap, low - prev_max)
            prev_max = high
        
        return max(max_gap, max_val - prev_max)




