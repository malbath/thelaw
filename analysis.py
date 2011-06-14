from sets import Set
import networkx as nx
import copy

def get_mr_x_position(graph, mr_x, move_cls):
    moves = mr_x.moves[:]
    moves.reverse()
    tickets = []
    visible_position = None
    for m in moves:
        if not m.target is None:
            visible_position = m.target
            break
        else:
            tickets.append(m.ticket)
    position = []
    tickets.reverse()
    if not visible_position is None:
        position = getPlaces(graph, visible_position, tickets)

    return position

def getPlaces(graph, position, tickets):
    if len(tickets) == 0:
        return [position]
    ticket = tickets[0]
    choices = graph.neighbors(position)
    places = []
    for c in choices:
        transport = graph[position][c]
        for t in transport:
            if transport[t]['ticket']==ticket:
                if len(tickets)==1:
                    places.append(c)
                else:
                    tix = tickets[:]
                    tix.pop(0)
                    places.extend(getPlaces(graph,c,tix))
    return list(set(places))

def getMrxRoutes(graph, policemen, mr_x, move_cls):
    posishs = get_mr_x_position(graph, mr_x, move_cls)
    return getRoutes(graph, policemen, posishs)

def getRoutes(graph, policemen, posishs):
    shortest_paths = []
    for cop in policemen:
        options = Move_Options(cop)
        co_posish = cop.moves[-1].target
        for posish in posishs:
            options.paths.append(nx.shortest_path(graph, co_posish, posish))
        shortest_paths.append(options)
    return shortest_paths

class Move_Options(object):
    paths = []
    def __init__(self, cop):
        self.cop = cop
        self.paths = []

    def __repr__(self):
        return "Cop %s can go %s" % (self.cop, self.paths)

    def longest(self):
        longest_paths = []
        length = 0
        for path in self.paths:
            if length < len(path):
                longest_paths = [path]
                length = len(path)
            elif length == len(path):
                longest_paths.append(path)
        return longest_paths

    def shortest(self):
        shortest_paths = []
        length = 200
        for path in self.paths:
            if length > len(path):
                shortest_paths = [path]
                length = len(path)
            elif length == len(path):
                shortest_paths.append(path)
        return shortest_paths

goodplaces = []

# returns a list of goodplaces
def get_goodplaces(graph):
    if len(goodplaces)==0:
        for node in nx.nodes(graph):
            got_bus = False
            got_taxi = False
            got_ubahn = False
            for edge in nx.edges(graph,node):
                for tries in [0,1,2]:
                    try:
                        ticket = graph[edge[0]][edge[1]][tries]['ticket']
                        if ticket == 'Bus':
                            got_bus = True
                        elif ticket == 'Taxi':
                            got_taxi = True
                        elif ticket == 'UBahn':
                            got_ubahn = True
                    except:
                        pass
            if got_bus & got_taxi & got_ubahn:
                goodplaces.append(node)
    return goodplaces

# returns a list of Move objects with
def go_to_goodplace(whenshow, graph, polices, mr_x, move_cls):
    getRoutes(graph, polices, get_goodplaces)