# Subsets

def longestPalindrome(s):
    longest = '';
    for x in range(0, len(s)):
        if len(longest) > len(s) - x:
            break;
        for k in range(x + 1, len(s) + 1):
            str = s[x:k];
            if (str == str[::-1]):
                if len(longest) < len(str):
                    longest = str;
                    continue;
    print(longest);
    

longestPalindrome('babad');
longestPalindrome('cbbd');

