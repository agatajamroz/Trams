
def readMap(filename):
    text = []
    lines = []
    line = []
    nrLine = False
    with open(filename, "r") as file:
        file = file.read().splitlines()
        
        for l in file:

            
            l = l.split(" ")
            
            
            if "line" in l[0]:

                ll=l[0]
                if nrLine:
                    lines.append(line)

                nrLine = ((ll[5:7]))
                
                line = [nrLine]
            
            elif nrLine and l[0] != "":
                line.append(l)

        lines.append(line)

    return lines