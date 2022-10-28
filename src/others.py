import os
import cgi
from datetime import datetime

from others.dijkstra import dijkstra_test
from others.floyd import floyd_test
from others.kruskal import kruskal_test
from others.prim import prim_test

print("Content-Type: text/plain; charset=UTF-8")
print("Status: 200")
print()


now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("Run at:", now)
print("Experiment 2: Dijkstra, Floyd, Kruskal and Prim")
print("=======================")

print("                       ")
dijkstra_test()
print("                       ")
floyd_test()
print("                       ")
kruskal_test()
print("                       ")
prim_test()