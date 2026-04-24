# 524. Longest Word in Dictionary through Deleting

def find_longest_word(s, d):
    '''
    type: s: str
    type: d: List[s]
    rtype: str
    '''

    def is_subseq(s, target):
        i, j = 0, 0
        while i < len(s) and j < len(target):
            if s[i] == target[j]:
                j += 1
            i += 1
        return j == len(target)

    result = ""
    d = sorted(d)
    for i in range(len(d)):
        l_result, l_word = len(result), len(d[i])
        if l_word < l_result or (l_word == l_result and d[i] >= result):
            continue
        if is_subseq(s, d[i]):
            result = d[i]
    return result
