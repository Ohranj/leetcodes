# Plus One

def plusOne(digits):
    val = ''.join(str(x) for x in digits);
    ans = int(val) + 1;
    return [int(x) for x in str(ans)]

plusOne([1, 2, 3]);
plusOne([9]);