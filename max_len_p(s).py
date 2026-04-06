def max_len_p(s):
    if len(s) < 2:
        return 1
    left, MAX = 0, 0
    dct = {}
    for i in range(len(s)):
        ch = s[i]
        if ch in dct and dct[ch] >= left:
            left = dct[ch] + 1
        dct[ch] = i
        now_len = i - left + 1
        if now_len > MAX:
            MAX = now_len
    return MAX

test = "ABCDEBCFGH"

print(max_len_p(test))