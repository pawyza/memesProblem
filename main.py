def getProfitableList(allLists):
    if len(allLists) != 0:
        id = 1
        for l in range(len(allLists)):
            if l != id:
                if allLists[id][1]  <  allLists[l][1]:
                        id = l
        return (allLists[id][2],set(allLists[id][0]))
    else:
        return (0, set())

def newPath(path, memes):
    path = ((path[0], memes[0]), path[1] + memes[1], path[2] + memes[2])
    return path

def calculate(usb_size, memes):
    usb_sizeMIB = usb_size * 1024
    allLists = []
    new = 0
    for m in range(len(memes)):
        if memes[m][2] <= usb_sizeMIB:
            allLists.append(memes[m])
        for l in range(new ,len(allLists)):
            for n in range(m+1, len(memes)):
                if allLists[l][2] + memes[n][2] <= usb_sizeMIB:
                    allLists.append(newPath(allLists[l],memes[n]))
        new = len(allLists)

    return getProfitableList(allLists)
