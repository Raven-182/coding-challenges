def isSubsequence( s: str, t: str) -> bool:
    long , short = 0, 0

    while short < len(s) and long < len(t):
        if s[short] == t[long]:
            short += 1
        long += 1
    return short == len(s)


#mobe through the shorter list and also the longer list since the items need to be in sequence
#when an item from the small list found, only then increment to search next, if all items are found the pointer will be the length of the string
