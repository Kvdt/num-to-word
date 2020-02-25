finray = []
convray = []


def num_to_word(num: int):
    endstr = ''
    tempray = []
    strnum = [str(num)]
    for i in strnum:
        for j in i:
            tempray.append(j)
        finray.append(tempray)
        tempray = []
    for i in finray:
        while len(i) % 3:
            i.insert(0, 0)
        convray.append([i[x:x + 3] for x in range(0, len(i), 3)])
    for i in convray:
        for x in range(len(i)):
            j = i[x]
            thisone = False
            zeroerror = True
            for p in range(len(j)):
                k = int(j[p])
                if k == 1:
                    if p == 0:
                        endstr += 'one hundred '
                    elif p == 1:
                        if int(j[p + 1]) == 0:
                            endstr += 'ten '
                        elif int(j[p + 1]) == 1:
                            endstr += 'eleven '
                        elif int(j[p + 1]) == 2:
                            endstr += 'twelve '
                        elif int(j[p + 1]) == 3:
                            endstr += 'thirteen '
                        elif int(j[p + 1]) == 4:
                            endstr += 'fourteen '
                        elif int(j[p + 1]) == 5:
                            endstr += 'fifteen '
                        elif int(j[p + 1]) == 6:
                            endstr += 'sixteen '
                        elif int(j[p + 1]) == 7:
                            endstr += 'seventeen '
                        elif int(j[p + 1]) == 8:
                            endstr += 'eighteen '
                        elif int(j[p + 1]) == 9:
                            endstr += 'nineteen '
                        thisone = True
                    elif p == 2 and not thisone:
                        endstr += 'one '
                elif not thisone:
                    if k == 2:
                        if p == 0:
                            endstr += 'two hundred '
                        elif p == 1:
                            endstr += 'twenty '
                        elif p == 2:
                            endstr += 'two '
                    elif k == 3:
                        if p == 0:
                            endstr += 'three hundred '
                        elif p == 1:
                            endstr += 'thirty '
                        elif p == 2:
                            endstr += 'three '
                    elif k == 4:
                        if p == 0:
                            endstr += 'four hundred '
                        elif p == 1:
                            endstr += 'forty '
                        elif p == 2:
                            endstr += 'four '
                    elif k == 5:
                        if p == 0:
                            endstr += 'five hundred '
                        elif p == 1:
                            endstr += 'fifty '
                        elif p == 2:
                            endstr += 'five '
                    elif k == 6:
                        if p == 0:
                            endstr += 'six hundred '
                        elif p == 1:
                            endstr += 'sixty '
                        elif p == 2:
                            endstr += 'six '
                    elif k == 7:
                        if p == 0:
                            endstr += 'seven hundred '
                        elif p == 1:
                            endstr += 'seventy '
                        elif p == 2:
                            endstr += 'seven '
                    elif k == 8:
                        if p == 0:
                            endstr += 'eight hundred '
                        elif p == 1:
                            endstr += 'eighty '
                        elif p == 2:
                            endstr += 'eight '
                    elif k == 9:
                        if p == 0:
                            endstr += 'nine hundred '
                        elif p == 1:
                            endstr += 'ninety '
                        elif p == 2:
                            endstr += 'nine '
                if k: zeroerror = False
            if len(i) - x == 2 and not zeroerror:
                endstr += 'thousand '
            elif len(i) - x == 3 and not zeroerror:
                endstr += 'million '
            elif len(i) - x == 4 and not zeroerror:
                endstr += 'billion '
            elif len(i) - x == 5 and not zeroerror:
                endstr += 'trillion '
            elif len(i) - x == 6 and not zeroerror:
                endstr += 'quadrillion '
            elif len(i) - x == 7 and not zeroerror:
                endstr += 'quintillion '
    return endstr

print(num_to_word(25152))
