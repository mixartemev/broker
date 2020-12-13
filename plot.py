import matplotlib.pyplot as myplt
myplt.subplot(2, 1, 1)
myplt.bar([2, 5, 6, 8], [5, 2, 3, 4])
myplt.subplot(2, 1, 2)
myplt.polar([2, 5, 6, 8], [5, 2, 3, 4])
myplt.xlabel('time in mins')
myplt.ylabel('distance in Kilo meters')
myplt.grid()
myplt.show()
