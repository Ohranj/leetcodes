# Group Anagrams

def groupAnagrams(strs):
    groups = {};
    for x in strs:
        s = ''.join(sorted(x));
        if s not in groups:
            groups[s] = [x];
            continue;
        groups[s].append(x);
    return groups.values();


groupAnagrams([["b"],[""],[""]])
groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]);