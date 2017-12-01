import csv
from collections import defaultdict
import sys, re, types, random, networkx, math

DAMPING_FACTOR = 0.85

class Node:
    def __init__(self, ID):
        self.ID = ID
        self.adjacent_nodes = set()
        self.indegree = 0
        self.outdegree = 0


adjacency_list = [Node(-1) for i in range(0,1000000)]

set_of_nodes = {-1}

def format_key(key):
    key = key.strip()
    if(key.startwith('"') and key.endwith('"')):
        key = key[1 : -1]
    return key

def find_node(ID):
    for i in range(0, len(list_of_nodes)):
        if(list[i].ID == ID):
            return i
    return -1


def parse_data(filename):

    reader = csv.reader(open(filename,'r'), delimiter = '\t')
    data = [row for row in reader]
    for row in enumerate(data):

        node_a = int(row[1][0])
        node_b = int(row[1][1])

        #print(node_b)
        
        set_of_nodes.add(node_a)
        set_of_nodes.add(node_b)

        adjacency_list[node_a].ID = node_a
        adjacency_list[node_a].adjacent_nodes.add(node_b)
        adjacency_list[node_a].outdegree = adjacency_list[node_a].outdegree + 1

        adjacency_list[node_b].ID = node_b
        adjacency_list[node_b].indegree = adjacency_list[node_b].indegree + 1
        

    for s in set_of_nodes:
        print(adjacency_list[s].ID, adjacency_list[s].adjacent_nodes)
        
if __name__ == '__main__':
    filename = 'myTestGraph.txt'
    parse_data(filename)
    
    #get_ranks()
