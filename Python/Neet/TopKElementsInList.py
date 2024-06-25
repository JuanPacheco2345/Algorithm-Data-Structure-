#Linear Solution
def topKFrequent(nums, k):
    #Using Bucket Sort
    count = {}
    freq = [[] for i in range(len(nums) + 1)] # -> [fixed # of slots which list the frequencies]
    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) -1, 0, -1): # The last index, and will go till index zero, in descesding order
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    

    
    
    #Or you can do heap, and set it to ascending order, and then heapify to get the top k elements -> (klogn)