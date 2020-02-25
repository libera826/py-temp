from temp import *
from time import sleep
from os import system
import graph

GRAPH_LEN = 10
data = []
graph = graph.Graph()
while True:
    if len(data) <= GRAPH_LEN:
        data.append(getTemp(-2))
    else:
        for i in range(GRAPH_LEN-1):
            data[i] = data[i+1]
        data[GRAPH_LEN-1] = getTemp(-2)

    print('CPU Package: \t',getTemp(-2),'°C')
    for i in range(getCpuCount()):
        print('Core',i,':\t',getTemp(i),'°C')

    graph.makeGraph(data)
    graph.showGraph(10) 

    sleep(1)
    system('clear')