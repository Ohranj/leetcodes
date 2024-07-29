# Roman to integer

conversion = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

def romanToInt(s):
    sum = 0;
    isLast = len(s) - 1;
    skip = False;
    for indx, x in enumerate(s):
        val = conversion[x];
        if (skip):
            skip = False;
            continue;
        
        if (indx == isLast):
            sum += val;
            break;

        nextVal = list(s)[indx + 1];

        if (x == 'I'):
            if (nextVal == 'V' or nextVal == 'X'):
                skip = True;
                val = conversion[nextVal] - val;
        
        if (x == 'X'):
            if (nextVal == 'L' or nextVal == 'C'):
                skip = True;
                val = conversion[nextVal] - val;
        
        if (x == 'C'):
            if (nextVal == 'D' or nextVal == 'M'):
                skip = True;
                val = conversion[nextVal] - val;

        sum += val;
    return sum;

romanToInt("IV");
romanToInt("III");

