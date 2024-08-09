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
    res = dict()
    for str in strs:
        count = []
        for s in str:
            count.append(ord('a') - ord(s))
        res


def duplicateInteger(nums):
    seen = []
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        else:
            seen.append(nums[i])
    return False





def isAnagram(s,t):
    s_hashMap = {}
    t_hashMap = {}
    if (len(s) != len(t)):
        return False
    
    for i in range(len(s)):
        s_hashMap[s[i]] = 1 + s_hashMap.get(s[i], 0)
        t_hashMap[t[i]] = 1 + t_hashMap.get(t[i], 0)
    
    for char in s_hashMap:
        if s_hashMap[char] != t_hashMap.get(char,0):
            return False
        
    return True





def twoIntegerSum(nums, target):
    diff_nums = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in diff_nums:
            return[diff_nums[diff], i]
        else:
            diff_nums[nums[i]] = i
    return []




def anagramGroups(strs):
    res = defaultdict(List)
    for str_from_strs in strs:
        alph_count = [0] * 26
        for s in str:
            alph_count[ord('a') - ord(s)] += 1
            #Tuples are immutable (cannot be modifed + can use as key)
        res[tuple(alph_count)].append(str_from_strs)
    return res.values()


def topKElementinList(nums,k):
    freq = [[]for i in range(len(nums) + 1)]
    map_nums = {}
    res = []
    for i in range(len(nums)):
        map_nums[nums[i]] = 1 + map_nums.get(nums[i], 0)
    
    for num,num_count in map_nums.items():
        freq[num_count].append(num)
    
    for j in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if (len(res) == k):
                return res
            





def encode(strs):
    encoded_string = ""
    for st in strs:
        length = len(st)
        encoded_string += str(str(length)+ "#" + st)
    return encoded_string


def decode(s):
    i = 0
    res = []
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
    return res



def encode(strs):
    encoded_string = ""

    for st in strs:
        length = len(st)
        encoded_string += str(str(length) + "#" + st)
    return encoded_string


def decode(s):
    i = 0
    res = []

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i: j])
        i = j + 1
        j = i + length
        res.append(s[i : j])
        i = j
    return res