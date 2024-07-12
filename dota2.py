def predictPartyVictory( senate: str) -> str:

    radiant = [i for i,x in enumerate(senate) if x == 'R' ]
    dire = [i for i,x in enumerate(senate) if x == 'D' ]
    next = len(senate)
    while radiant and dire:
        if radiant[0] < dire[0]:
            radiant.append(next)
        else:
            dire.append(next)
        next += 1
        radiant.pop(0)
        dire.pop(0)
    return "Radiant" if radiant else "Dire"

print(predictPartyVictory('RD'))