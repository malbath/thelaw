__author__ = 'Tarik'
import logging
import random

class SimpleController(object):
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

  