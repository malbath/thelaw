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
        return []
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

def getRoutes(graph, policemen, mr_x, move_cls):
    posishs = get_mr_x_position(graph, mr_x, move_cls)
    shortest_paths = []
    for cop in policemen:
        options = Move_Options(cop)
        for posish in posishs:
            co_posish = cop.moves[-1].target
            options.paths.append(nx.shortest_path(graph, co_posish, posish))
        shortest_paths.append(options)
        print 'shortest_path', options.cop, options.shortest()

    print 'Police', policemen
    print 'MRX', mr_x
    print 'moves', move_cls

class Move_Options(object):
    paths = []
    def __init__(self, cop):
        self.cop = cop

    def __repr__(self):
        return "Cop %s can go %s" % (self.cop, self.paths)

    def shortest(self):
        shortest_paths = []
        length = 200
        for path in self.paths:
            if length > len(path):
                shortest_paths = [path]
            elif length == len(path):
                shortest_paths.append(path)
        return shortest_paths
