
def mahoa(cr):
    kq = ""
    D_mahoa = {0:"n",1:"x",2:"o"}
    dem = 0
    luu = None
    for row in cr.diagram:
        for cell in row:
            if cell == luu:
                dem += 1
            else:
                if dem > 1:
                    kq += str(dem)
                luu = cell
                kq += D_mahoa[cell]
                dem = 1
    if dem > 1:
        kq += str(dem)
    return kq

# from caro import caro
# cr = caro(10,10)
# from napbanco import napbanco
# napbanco(cr)
# print(mahoa(cr))