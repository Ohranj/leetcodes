# Find the Index of the First Occurence in a String

def strStr(haystack, needle):
    indx = -1;
    cutoff = len(haystack) - len(needle) + 1;
    for i in range(0, cutoff):
        stopAt = i + len(needle);
        if haystack[i:stopAt] == needle:
            indx = i;
            break;
    return indx;
                

res = strStr('sadbutsad', 'sad');
print(res);

res = strStr('leetcode', 'leeto');
print(res);

res = strStr('hello', 'll');
print(res);

res = strStr('a', 'a');
print(res);