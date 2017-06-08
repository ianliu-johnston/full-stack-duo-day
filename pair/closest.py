#!/usr/bin/python3

def get_distance(coord_a=(0,0), coord_b=(0,0)):
    a = float(coord_a[0] - coord_b[0])
    b = float(coord_a[1] - coord_b[1])
    return((a ** 2 + b ** 2) ** 0.5)






if __name__ == "__main__":
    lst1 = [(4,2),(1,6),(1,2),(1,3),(5,6),(1,1),(0,2),(2,3)]
    lst2 = [(-1,-5),(4,3),(3,-6),(4,-6),(7,3),(0,1),(3,3),(6,-2)]

    lst = lst2
    j = 0
    dst = {}
    for (i, coord_a) in enumerate(lst):
        j = i + 1
        while j < len(lst):
            coord_b = lst[j]
            dst.update({get_distance(coord_a, coord_b): [coord_a, coord_b]})
            j += 1
    print("{:f}:".format(min(dst)), dst.get(min(dst)))
