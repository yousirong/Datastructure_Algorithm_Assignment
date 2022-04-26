def hanoiTower(n, source, dest, temp):
    if (n == 1):
        print( "Move a disk from peg %d to peg %d" % (source, dest))
        # print( "Move a disk from peg {0} to peg {1}".format(source, dest))
    else:
        hanoiTower(n-1, source, temp, dest)
        print( "Move a disk from peg %d to peg %d" % (source, dest))
        hanoiTower(n-1, temp, dest, source)

print("n = 1")
hanoiTower(1,1,3,2)

print("n = 2")
hanoiTower(2,1,3,2)

print("n = 3")
hanoiTower(3,1,3,2)
