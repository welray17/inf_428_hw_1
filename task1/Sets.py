class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set()
        for i in range(0, len(nums1)):
            set1.add(nums1[i])

        set2 = set()
        for i in range(0, len(nums2)):
            set2.add(nums2[i])
        
        result_set = set()
        for num in set1:
            if num in set2:
                result_set.add(num)
        return list(result_set)
        
