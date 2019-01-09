from gauss import Gauss
from square_roots import SquareRoots
from running import Running
from lt_rotation import LtRotation
from ui import UI
from termcolor import colored
import time

eps = 0.001

'''task 1'''
t1 = colored('TASK1', 'red')
print(t1)
a = [
    [-54, -11, 40, 57, 80, -99, 29, 45, 22, 50],
    [19, 40, 89, -36, -63, 22, 57, -62, -14, 39],
    [-81, 40, 69, -87, -89, -63, 76, 31, 43, -27],
    [18, 42, -69, -88, -37, 31, 91, 91, -37, 14],
    [9, -71, 78, 98, -83, 98, 45, 27, -10, 20],
    [38, -57, 65, -97, 49, 39, -3, 18, 43, 98],
    [-62, 0, 72, -22, -43, 58, 87, 26, 64, 72],
    [60, 61, 68, -14, -28, 60, -8, 36, 40, -34],
    [73, 17, 62, 15, -46, -22, 71, -50, 72, 38]
]
UI.print_slar(a, 9)
start_time = time.time()
g1 = Gauss(a, 9, eps)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
lu = LtRotation(a, 9, eps)
print("--- %s seconds ---" % (time.time() - start_time))

'''task 2'''
t2 = colored('TASK2', 'red')
print(t2)
b = [
    [414, 250, -51, -38, -129, -77, 208, -8, 239, 259, 240],
    [250, 655, 293, 108, -42, 255, -91, -26, 47, 200, 353],
    [-51, 293, 643, 184, -228, 94, -22, -117, -141, -235, 284],
    [-38, 108, 184, 265, -32, -96, -210, 126, 12, -167, 346],
    [-129, -42, -228, -32, 282, 127, -169, 40, 7, 44, -219],
    [-77, 255, 94, -96, 127, 466, -162, -98, -248, 169, 219],
    [208, -91, -22, -210, -169, -162, 678, -10, 260, -116, 451],
    [-8, -26, -117, 126, 40, -98, -10, 655, 22, -166, 205],
    [239, 47, -141, 12, 7, -248, 260, 22, 480, -28, 528],
    [259, 200, -235, -167, 44, 169, -116, -166, -28, 583, 361]
]
UI.print_slar(b, 10)
start_time = time.time()
sq = SquareRoots(b, 10, eps)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
g2 = Gauss(b, 10, eps)
print("--- %s seconds ---" % (time.time() - start_time))

t3 = colored('TASK3', 'red')
print(t3)
c = [
    [346, -16, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [-65, 248, -80, 0, 0, 0, 0, 0, 0, 0, -137],
    [0, 176, 660, 286, 0, 0, 0, 0, 0, 0, 996],
    [0, 0, -249, -785, -315, 0, 0, 0, 0, 0, 624],
    [0, 0, 0, -6, -20, 8, 0, 0, 0, 0, -29],
    [0, 0, 0, 0, -365, -802, 46, 0, 0, 0, 789],
    [0, 0, 0, 0, 0, -102, 545, -175, 0, 0, -725],
    [0, 0, 0, 0, 0, 0, -93, -322, 3, 0, -220],
    [0, 0, 0, 0, 0, 0, 0, 105, 813, -324, 855],
    [0, 0, 0, 0, 0, 0, 0, 0, -194, -218, 835]
]
UI.print_slar(c, 10)
start_time = time.time()
run = Running(c, 10, eps)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
g3 = Gauss(c, 10, eps)
print("--- %s seconds ---" % (time.time() - start_time))
