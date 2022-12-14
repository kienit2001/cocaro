def docfile(name):
    f = open(name, "r")
    data = f.readlines()
    f.close()
    D_data = {}
    for i in data:
        vt = i.find("|")
        if vt == -1:
            key = ""
            value = list(map(int, i.split()))
        else:
            key = i[:vt].strip()
            value = list(map(int, i[vt + 1:].split()))
        D_data[key] = value
    return D_data


def vtmax(L):
    vt = None
    for i in range(len(L)):
        if vt is None or L[vt] < L[i]:
            vt = i
    return vt


def minimax(key, chieusau, b_max, root, alpha):
    L = data[key]
    if root:
        kq = None
        L_kq = []
        for i in range(len(L)):
            if chieusau != 1:
                nhanh = minimax(str(i), chieusau - 1, not b_max, False,None if kq== None else kq -1)
            else:
                nhanh = L[i]
            if nhanh != None:
                if kq == None or nhanh > kq:
                    L_kq = [i]
                    kq =nhanh
                elif kq == nhanh:
                    L_kq.append(i)
        return L_kq
    else:
        kq = None
        for i in range(len(L)):
            if chieusau != 1:
                nhanh = minimax(key + " " + str(i), chieusau - 1, not b_max, False, kq)
            else:
                nhanh = L[i]
            if nhanh != None:
                if b_max:
                    if kq == None or nhanh > kq:
                        kq = nhanh
                    if alpha != None and kq >= alpha:
                        return None
                else:
                    if kq == None or nhanh < kq:
                        kq = nhanh
                    if alpha != None and kq <= alpha:
                        return None
        return kq


data = docfile("minimax1.txt")
print(data)
print(minimax("", 1, True, True, None))
