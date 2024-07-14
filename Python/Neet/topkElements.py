def topKFrequent(nums, k):
   count = {}
   freq  = [[] for i in range(len(nums))]
   res = []
   
   for num in nums:
        count[num] = 1 + count.get(num,0)
   for n,c in count.items():
        freq[c].append(n)
    
   for i in range(len(freq) - 1, 0, -1):
       for val in freq[i]:
           res.append(val)
           if len(res) == k:
               return res
 