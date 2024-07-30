# Longest Common Prefix

def longestCommonPrefix(strs):
    maxIterate = min(strs, key = len);
    prefix = '';
    isMatch = True;
    current = '';
    for x in range(len(maxIterate)):
        isMatch = True;
        current = '';
        for k in range(len(strs)):
            if (not current):
                current = strs[k][x];
                continue;
            if (current != strs[k][x]):
                isMatch = False;
                break;
        if (isMatch):
            prefix += current;
            continue;
        break;
    return print(prefix) if prefix else print("");



longestCommonPrefix(['flower', 'flow', 'flight']);
longestCommonPrefix(['dog', 'racecar', 'car']);