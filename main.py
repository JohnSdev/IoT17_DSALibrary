
from graph import Graph
from sort import *
import random
import time

g = Graph()
g.addVertex("STHLM")
g.addVertex("OREBRO")
g.addVertex("LIDK")
g.addVertex("GBG")
g.addVertex("HELBG")
g.addVertex("LUND")
g.addVertex("KRIST")
g.addVertex("JONK")
g.addVertex("LINK")

g.addEdge( "STHLM",  "OREBRO", 75 )
g.addEdge( "OREBRO", "LIDK",   25 )
g.addEdge( "LIDK",   "GBG",    50 )
g.addEdge( "GBG",    "HELBG",  5 )
g.addEdge( "HELBG",  "LUND",   5 )
g.addEdge( "LUND",   "KRIST",  20 )
g.addEdge( "KRIST",  "JONK",   15 )
g.addEdge( "HELBG",  "JONK",   35 )
g.addEdge( "JONK",   "LINK",   100 )
g.addEdge( "LINK",   "STHLM",  30 )

#print( g.findCheapestPath( "STHLM", "LUND" ) )

mylist = []
list2 = []
for x in range(0,100000):
    mylist.append(random.randint(0,999))

for x in range(0,200000):
    list2.append(random.randint(0,999))


time1=time.time()
shellSort(mylist)
time2=time.time()
print("Shell enkel = {:.4f}".format(time2-time1))

time1=time.time()
shellSort(list2)
time2=time.time()
print("Shell dubbel= {:.4f}".format(time2-time1))
