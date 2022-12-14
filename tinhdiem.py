from caro import caro

L_4_huong = [(-1,-1),(-1,0),(-1,1),(0,-1)]
doi12 = {1:2,2:1}

def doi_caroxo(cr):
    if cr :
        return 1
    else:
        return 2



def demotrong(cr,x,y,xm,ym,slquan):
    kq = 0
    while (cr.diagram[y][x] == 0):
        kq += 1
        if slquan + kq > 3:
            return kq
        x += xm
        y += ym
        if not (0 <= x < cr.r and 0 <= y < cr.c):
            break
    # while (cr.diagram[y][x] == 0):
    #     kq += 1
    #     if slquan + kq > 3:
    #         return kq
    #     x -= xm
    #     y -= ym
    #     if not (0 <= x < cr.r and 0 <= y < cr.c):
    #         break
    return kq

def diemo_huong(cr,x,y,xm,ym):
    x0,y0 = x,y
    quanco = cr.diagram[y][x]
    huong1 = 1
    dem = 0
    nhaycach = False
    while True:
        x += xm
        y += ym
        if not(0 <= x < cr.r and 0 <= y < cr.c) or cr.diagram[y][x] == doi12[quanco]:
            huong1 = 0
            break
        if cr.diagram[y][x] == 0:
            if nhaycach:
                break
            else:
                x_nhaycach = x + xm
                y_nhaycach = y + ym
                if (0 <= x_nhaycach < cr.r and 0 <= y_nhaycach < cr.c) and cr.diagram[y_nhaycach][x_nhaycach] == quanco:
                    nhaycach = True
                    continue
                break
        dem += 1
    xh1, yh1 = x , y
    x,y = x0,y0
    huong2 = 1
    nhaycach2 = False
    while True:
        x -= xm
        y -= ym
        if not(0 <= x < cr.r and 0 <= y <cr.c) or cr.diagram[y][x] == doi12[quanco] :
            huong2 = 0
            break
        if cr.diagram[y][x] == 0:
            if nhaycach2:
                break
            else:
                x_nhaycach = x - xm
                y_nhaycach = y - ym
                if (0 <= x_nhaycach < cr.r and 0 <= y_nhaycach < cr.c) and cr.diagram[y_nhaycach][x_nhaycach] == quanco:
                    nhaycach2 = True
                    continue
                break
        dem += 1
    xh2, yh2 = x , y
    if huong1 == 1:
        sltrong = demotrong(cr,xh1,yh1,xm,ym,dem)
        #print("so luonh trong ",sltrong, dem)
        if sltrong+dem <= 3:
            huong1 = 0
    if huong2 == 1:
        sltrong = demotrong(cr,xh2,yh2,-xm,-ym,dem)
        #print("so luonh trong ",sltrong, dem)
        if sltrong+dem <= 3:
            huong2 = 0
    if dem > 3:
        dem = 3
    if nhaycach or nhaycach2: kqcach = 0.75
    else: kqcach = 1
    #print(dem,huong1,huong2)
    return 3**dem*(huong1+huong2)*kqcach
def diem0(cr,x,y):
    kq = 0
    for xm,ym in L_4_huong:
        kq += diemo_huong(cr,x,y,xm,ym)
        #print(kq)
    return kq

def tinhdiem(cr,x0):
    D_kq = {
        1:0,2:0
    }
    trai, phai, tren, duoi = cr.lay_gh()
    #print(trai, phai, tren, duoi)
    if trai != None:
        for y in range(tren,duoi+1):
            for x in range(trai,phai+1):
                #print(1000000000)
                if cr.diagram[y][x] != 0:
                    D_kq[cr.diagram[y][x]] += diem0(cr,x,y)
                    #print(D_kq)

    #print(danhtruoc)
    #print(D_kq[danhtruoc])
    D_kq[doi_caroxo(cr.xo)] *= 2
    #print(D_kq[1])
    #print(D_kq)
    return D_kq[x0] - D_kq[doi12[x0]]



# cr = caro(10,10)
# from napbanco import napbanco
# napbanco(cr)
# print(tinhdiem(cr,1))
#
# a = doi_caroxo(cr.xo)

# while cr.chay():
#     # print(tinhdiem(cr,1))
#     if a != doi_caroxo(cr.xo):
#         print(tinhdiem(cr,1))
#         a = doi_caroxo(cr.xo)
#         print("ghet mot nuoc")