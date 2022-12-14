import numpy
from caro import caro

def napbanco(cr):
    f = open("banco.txt","r")
    data = f.readlines()
    f.close()
    print(data)

    diagram = []
    for i in data:
        i = i.split()
        for j in range(len(i)):
            i[j] = int(i[j])
        diagram.append(i)
    print(diagram)
    print(numpy.array(diagram))



    cr.nap_diagram(diagram,1)

