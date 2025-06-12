import sys
import os

if len(sys.argv) > 1:
    a = sys.argv[1:]
    k = 0
    g = ''
    coun = False
    nu = False
    sor = False
    for i in a:
        if ".txt" in i:
            k += 1
            g = i
        if i == "--num":
            nu = True
        if i == "--count":
            coun = True
        if i == "--sort":
            sor = True
    if k == 0:
        print("ERROR")
        sys.exit()
    if not os.path.exists(g):
        print("ERROR")
        sys.exit()
    with open(g) as f:
        a = f.read().split("\n")
        if sor:
            a.sort()
        if nu:
            for i in range(len(a)):
                a[i] = str(i) + " " + a[i]
        print(*a, sep='\n')
        if coun:
            print(f"rows count: {len(a)}")