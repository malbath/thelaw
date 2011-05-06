from sets import Set
import copy

def get_mr_x_position(graph, mr_x):
    moves = mr_x.moves[:]
    print moves
    moves.reverse()
    tickets = []
    visible_position = None
    for m in moves:
        if not m.target is None:
            visible_position = m.target
            break
        else:
            tickets.append(m.ticket)
    position = None
    tickets.reverse()
    if not visible_position is None:
        print visible_position, tickets
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