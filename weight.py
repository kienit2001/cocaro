
def doc_weight(muc):
    f = open("weight"+str(muc)+".txt","r")
    data = f.readlines()
    f.close()
    L = []
    D = {}
    for i in data:
        vt = i.find("|")
        key = i[:vt]
        L_nuoc_di = i[vt+1:].split()
        for move in L_nuoc_di:
            vt = move.find(",")
            x = int(move[:vt])
            y = int(move[vt+1:])
            L.append((x,y))
        D[key] = L
    return D

def ghi_weight(key,L,muc):
    chuoi = ""
    for x,y in L:
        chuoi += str(x) + "," + str(y) + " "
    f = open("weight"+str(muc)+".txt", "a")
    f.write(key + "|" + chuoi + "\n")
    f.close()
