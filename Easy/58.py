# Length of Last Word

def lengthOfLastWord(s):
    arr = s.split(' ')
    res = list(filter(lambda x: x, arr))[-1];
    print(len(res));
  

lengthOfLastWord('   fly me   to   the moon  ');