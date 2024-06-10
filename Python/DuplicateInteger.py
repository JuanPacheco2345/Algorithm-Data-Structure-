def hasDuplicate(nums):
    seen = []
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.append(nums[i])
    return False

def twoSum(nums, target):
    #Two Sums on Neetcode
    res = set()
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in res:
            return [i, res[diff]]
        else:
            res[nums[i]] = i
    return []

def maxProfit(prices):
    maxProfit = 0
    l = 0
    r = 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1

    return maxProfit
        
def isAnagram(s,t):
    sMapping = {}
    tMapping = {}
    if len(s) != len(t):
        return False
    for s_char in s:
        sMapping[s_char] = 1 + sMapping.get(s_char,0)
        tMapping[s_char]  = 1 + tMapping.get(s_char,0)
    
    for s_char in s:
        if sMapping[s_char] != tMapping.get(0,s_char):
            return False
    return True


def isValid(s):
    #Code Here
    stack = []