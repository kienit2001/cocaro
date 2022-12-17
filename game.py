from caro import caro
from napbanco import napbanco
from sapxep import sapxep,doi_caroxo
from weight import doc_weight,ghi_weight
from mahoa import mahoa
import random
import numpy


# xo = cr.xo
# print(numpy.array(cr.diagram))
cr_main = caro(15, 15)
cr_chayngam = caro(cr_main.r,cr_main.c)


def minimax(cr, chieusau, b_max, root, alpha,quan):
    L = sapxep(cr,quan)
    cr_main.cho()
    # print(L)
    if root:
        diem = L[0][0]
        # print("asvdjgsadkjhaslkdj",L[0])
        #x,y = L[0][1]
        if diem == "x" or diem == "o":
            return [L[1]]
        kq = None
        L_kq = []
        for diem,toando in L:
            if chieusau != 1:
                x,y = toando
                cr.botmove(x,y)
                nhanh = minimax(cr, chieusau - 1, not b_max, False, None if kq == None else kq - 1 if b_max else kq + 1,
                                quan)
                cr.undo()
            else:
                nhanh = diem
            if nhanh != None:
                if b_max and (kq == None or nhanh > kq):
                    L_kq = [toando]
                    kq =nhanh
                elif not b_max and (kq == None or nhanh < kq):
                    L_kq = [toando]
                    kq = nhanh
                elif kq == nhanh:
                    L_kq.append(toando)
        return L_kq
    else:
        diem = L[0][0]
        #x, y = L[0][1]
        if diem == "x" or diem == "o":
            return 100000 if diem == "x" else -100000
        kq = None
        for diem,toando in L:
            if chieusau != 1:
                x, y = toando
                cr.botmove(x, y)
                nhanh = minimax(cr, chieusau - 1, not b_max, False, kq, quan)
                cr.undo()
            else:
                return diem
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



def maydi(dothongminh,danh):
    if cr_main.lay_gh()[0] == None:
        x,y = cr_main.r//2,cr_main.c//2
    else:
        D_weight = doc_weight(dothongminh)
        hinhco = mahoa(cr_main)
        if hinhco in D_weight:
            print("da co hinh")
            L = D_weight[hinhco]
        else:
            cr_chayngam.nap_diagram(cr_main.diagram,cr_main.xo)
            # print(cr_main.xo)
            #cr_chayngam.chay()
            L = minimax(cr_chayngam, dothongminh, cr_chayngam.xo, True, None, danh)
            D_weight[hinhco] = L
            ghi_weight(hinhco,L,dothongminh)
        print("nhung nuoc di toi uu", L)
        x, y = random.choice(L)
    cr_main.botmove(x,y)


#napbanco(
#xo = doi_caroxo(cr.xo)
def danhvoiamy(cap,danhvoimay):
    cr_main.run = True
    cr_main.reset()
    while cr_main.chay():
        #print("--------------------------",doi_caroxo(cr.xo))
        if cr_main.chay() == 100000 or cr_main.chay() == -100000:
            break
        # print("-----------------", cr_main.result)

        if cr_main.thang:
            if doi_caroxo(cr_main.xo) == danhvoimay:
                # print("-----------------",cr_main.result)
                maydi(cap, danhvoimay)


def maytudanh(cap):
    while cr_main.chay():
        # print("--------------------------",doi_caroxo(cr.xo))
        if cr_main.result != 0:
                 cr_main.reset()
        maydi(cap, 1)

def choi2nguoi():
    cr_main.run = True
    cr_main.reset()
    while cr_main.chay():
        pass
# vsmay = input("nhap 1 la danh voi may:")
# if vsmay == "1":
#     xo = input("nhap 1 neu may danh x 2 may danh o:")
# cr_main = caro(20, 20)
# cr_chayngam = caro(cr_main.r,cr_main.c)
# D_weight = doc_weight()
# while cr_main.chay():
#     #print("--------------------------",doi_caroxo(cr.xo))
#     if vsmay == "1":
#         if doi_caroxo(cr_main.xo) == int(xo):
#             if cr_main.result == 0:
#                 maydi(3)
#     else:
#         if cr_main.result != 0:
#             cr_main.reset()
#         maydi(3)
#         #xo = doi_caroxo(cr.xo)