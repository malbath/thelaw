import analysis
from start import Move
from thelaw.analysis import try_to_catch, evaluate_ticket

__author__ = 'Tarik'
import logging
import random

class SimpleController(object):
    mr_x_position = None
    logger = None

    def __init__(self, graph, mr_x, polices, move_cls, logger):
        self.graph = graph
        self.mr_x = mr_x
        self.polices = polices
        self.move_cls = move_cls
        self.logger = logger

    def draw(self, round, who):
        choices = self.graph.neighbors(who.get_position())
        r = random.randint(0, len(choices)-1)
        target = choices[r]
        move_type = self.graph[who.get_position()][target][0]['ticket']
        if who.tickets_cab==1:
            who.tickets_cab = 2
        return self.move_cls(target, move_type)

class TicketOrganizer:
    def __init__(self, graph, mr_x, polices, move_cls):
        self.graph = graph
        self.mr_x = mr_x
        self.polices = polices
        self.move_cls = move_cls

    def draw(self, round, who):
        choices = self.graph.neighbors(who.get_position())
        r = random.randint(0, len(choices)-1)
        target = choices[r]
        move_type = self.graph[who.get_position()][target][0]['ticket']
        if who.tickets_cab == 0 :
			self.graph[who.get_position()][target][0]['ticket'] = 'bus'
			move_type = self.graph[who.get_position()][target][0]['ticket']
        if who.tickets_bus == 0 :
			self.graph[who.get_position()][target][0]['ticket'] = 'underground'
			move_type = self.graph[who.get_position()][target][0]['ticket']
			return self.move_cls(target, move_type)
        else :
			return self.move_cls(target, move_type)

class PipediController(object):
    mr_x_position = None
    logger = None
    evaluator = None

    def __init__(self, graph, mr_x, polices, move_cls, logger):
        self.graph = graph
        self.mr_x = mr_x
        self.polices = polices
        self.move_cls = move_cls
        self.logger = logger

    # returns a list of Move objects with index cop
    def evaluate_draws(self, round):
        whenshow = (round+3)%5
        if round < 2:
            return analysis.go_to_goodplace(whenshow, self.graph, self.polices, self.mr_x, self.move_cls)
        elif whenshow == 3 | whenshow == 4:
            draws = analysis.go_to_goodplace()
            shortest_paths = analysis.getRoutes(self.graph, self.polices, self.mr_x, self.move_cls)
            for path_option in shortest_paths:
                temp_draw = None
                temp_nodes_count = 200
                for path in path_option.paths:
                    if len(path) < 2 & len(path) < temp_nodes_count:
                        temp_nodes_count = len(path)
                        temp_draw = Move(path[0], evaluate_ticket(path_option.cop, path[0]))
                if temp_draw != None:
                    draws[path_option.cop] = temp_draw
            return draws
        else:
            return try_to_catch(self.graph, self.polices, self.mr_x, self.move_cls)

    def draw(self, round, who):
        if self.evaluator == None:
            self.evaluator = who
        if self.evaluator == who:
            self.draws = self.evaluate_draws(round)
        for draw in self.draws:
            if draw.cop == who:
                print(draw)
                return draw