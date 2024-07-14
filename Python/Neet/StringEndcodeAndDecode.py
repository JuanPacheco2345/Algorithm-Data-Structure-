def encode(strs):
    encode_strs = ""
    for s in strs:
        length = len(s)
        encode_strs += str(str(length) + "#" + s)
    return encode_strs



def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i : j])
        i = j
    return res
        
