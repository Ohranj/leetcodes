# Valid Parenthesis


chars = {
    '(': ')',
    '{': '}',
    '[': ']',
}

def isValid(s: str):
    values = [];
    valid = False;

    for x in s:
        if x in chars:
            values.append(x);
            valid = True;
            continue;

        try:
            lastOpener = chars[values[-1]];
            if (lastOpener == x):
                values.pop();
                continue;
            raise Exception()
        except:
            valid = False;
            break;
    return valid;


res = isValid('()()')
print(res);

res = isValid('(())[}]')
print(res);