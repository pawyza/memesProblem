def getProfitableList(allLists):
    """Function that gives best combination of memes from possible combinations

    Args:
        allLists : list(list(str),int,int)
            List containing all possible combinations of memes. Each element
            contains list of memes names, memes size in MiB and memes value

    Return:
        tuple(int,set(str))
            Tuple containing total value of memes combination and set of memes names
            in that combination
    """
    if len(allLists) != 0:
        id = 1
        for l in range(len(allLists)):
            if l != id:
                if allLists[id][1]  <  allLists[l][1]:
                        id = l
        return (allLists[id][2],set(allLists[id][0]))
    else:
        return (0, {})


def checkIfInList(memesIn, newMeme):
    """Function that check if newMeme is already in memesIn list

    Args:
        memesIn : list(str)
            List containing all memes names in current combination
        newMeme : str
            New meme name that we check if already is in memesIn

    Return:
        boolean
            If True memesIn contains newMeme, if False it doesn't
    """
    for m in range(len(memesIn)):
        if memesIn[m] == newMeme:
            return True

    return False

def checkIfSame(memes1,memes2):
    """Function that check if memes1 and memes2 are the same combinations in
    different order

    Args:
        memes1 : list(str)
            List of memes names
        memes2 : list(str)
            List of memes names

    Return:
        boolean
            If True memes1 and memes2 have identical elements, if False they
            are different combinations
    """
    for m in range(len(memes2)):
        if memes2[m] not in memes1:
            return False

    return True

def eliminateRep(memesAll, memes2):
    """Function that check if memesAll already contains memes2 combination

    Args:
        allLists : list(list(str),int,int)
            List containing already found combinations of memes. Each element
            contains list of memes names, memes size in MiB and memes value
        memes2 : tuple(list(str),int,int)
            Tuple containing new possible combination of memes. Tuple contains
            list of memes names, theirs size in MiB, their value

    Return:
        boolean
            If True allLists already contains memes2 combination, if False
            memes2 is completly new combination
    """
    for l in range(len(memesAll)):
        if len(memesAll[l][0]) == len(memes2[0]):
            if checkIfSame(memesAll[l][0],memes2[0]):
                return True

    return False

def newPath(path, memes):
    """Function creates new combination from old combinations and given meme

    Args:
        path : tuple(list(str),int,int)
            List containing old possible combination of memes. Tuple
            contains list of memes names, memes size in MiB and memes value
        memes : tuple(str,int,int)
            Tuple containing meme. Tuple contains memes name, memes size in MiB,
             memes value

    Return:
        tuple(list(str),int,int)
            Tuple containing new possible combination of memes. Tuple contains
            list of memes names, theirs size in MiB, their value
    """
    if path[0] == []:
        return ([memes[0]], path[1] + memes[1], path[2] + memes[2])
    else:
        return (path[0] + [memes[0]], path[1] + memes[1], path[2] + memes[2])

def calculate(usb_size, memes):
    """Function used for creating most profitable combination of memes that can
    fit into given USB

    Args:
        usb_size : int
            Given USB size in GiB
        memes : list(tuple(str,int,int))
            List of given memes. Each tuple contains memes name,
            memes size in MiB, memes value

    Return:
        tuple(int,set(str))
            Tuple containing total value of memes combination and set of memes names
            in that combination
    """
    usb_sizeMIB = usb_size * 1024
    allLists = []
    new = 0

    for m in range(len(memes)):
        allLists.append(newPath([list(),0,0],memes[m]))

    for max in range(len(memes)-1):
        for m in range(len(allLists)):
            for n in range(len(memes)):
                if allLists[m][1] + memes[n][1] <= usb_sizeMIB and not checkIfInList(allLists[m][0], memes[n][0]):
                    if not eliminateRep(allLists,newPath(allLists[m],memes[n])):
                        allLists.append(newPath(allLists[m],memes[n]))
        new = len(allLists)

    return getProfitableList(allLists)
