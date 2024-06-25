from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        #There are 26 lower case character
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()



groupAnagrams(["act","pots","tops","cat","stop","hat"])