def defDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

def isAnagram(s,t):
    t_hash = {}
    s_hash = {}

    #Non Equal Size Case
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        s_hash[s[i]] = (1 + s_hash.get(s[i]), 0)
        t_hash[t[i]] = (1 + t_hash.get(t[i]), 0)

    for i in range(len(s)):
        if s_hash[s[i]] != t_hash.get(s[i],0):
            return False
    
    return True



def twoSum(nums,target):
    sumRecords = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in sumRecords:
            return [i,sumRecords[diff]]
        else:
          sumRecords[nums[i]] = i
    return False  


def anagramGroups(strs):
    
