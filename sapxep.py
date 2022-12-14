from tinhdiem import tinhdiem,doi_caroxo

def sapxep(cr):
    L_nuoc_di =  cr.lay_L_nuoc_di()
    L_ket_qua = []
    for x,y in L_nuoc_di:
        cr.botmove(x,y)
        if cr.result == 0:
            L_ket_qua.append([tinhdiem(cr,1),(x,y)])
        elif cr.result == 1:
            cr.undo()
            return ["x",(x,y)]
        elif cr.result == 2:
            cr.undo()
            return ["o",(x,y)]
        else:
            L_ket_qua.append([0,(x,y)])
        cr.undo()
    if doi_caroxo(cr.xo) == 1:
        L_ket_qua.sort(reverse = True)
    else:
        L_ket_qua.sort()
    return L_ket_qua

# from caro import caro
# cr = caro(10,10)
# xo = doi_caroxo(cr.xo)
# while cr.chay():
#     if xo != doi_caroxo(cr.xo):
#         xo = doi_caroxo(cr.xo)
#         print(sapxep(cr))