"""
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.
"""

def containsCloseNums(nums, k):
    previous_seen = {}
    for idx, val in enumerate(nums):
        if val in previous_seen:
            if idx - previous_seen[val] <= k:
                return True
        
        # Store current
        previous_seen[val] = idx
    
    return False
                
            
        
        
