__author__ = 'Tarik'
import logging
import random
import analysis

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
        self.distances = []

    def draw(self, round, who):
	choices = self.graph.neighbors(who.get_position())

	r = random.randint(0, len(choices)-1)

	target = choices[r]
	if round > 2 :
		if who.name == "Police 1":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[0].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 2":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[1].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 3":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[2].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 4":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[3].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 5":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[4].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		
	
	move_type = self.graph[who.get_position()][target][0]['ticket']
		
	if who.tickets_cab < who.tickets_bus :
		self.graph[who.get_position()][target][0]['ticket'] = 'bus'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if  who.tickets_bus < who.tickets_cab :
		self.graph[who.get_position()][target][0]['ticket'] = 'cab'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if who.tickets_cab == who.tickets_bus :
		self.graph[who.get_position()][target][0]['ticket'] = 'cab'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if who.tickets_bus == 0 :
		self.graph[who.get_position()][target][0]['ticket'] = 'cab'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if round == 3 :
		self.graph[who.get_position()][target][0]['ticket'] = 'underground'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if round == 8 :
		self.graph[who.get_position()][target][0]['ticket'] = 'underground'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if who.tickets_bus == 0 and who.tickets_cab == 0 :
		self.graph[who.get_position()][target][0]['ticket'] = 'underground'
		move_type = self.graph[who.get_position()][target][0]['ticket']
		#print who.tickets_bus
		#print who.tickets_cab
	return self.move_cls(target, move_type)
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
        self.distances = []

    def draw(self, round, who):
	choices = self.graph.neighbors(who.get_position())

	r = random.randint(0, len(choices)-1)

	target = choices[r]
	if round > 2 :
		if who.name == "Police 1":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[0].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 2":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[1].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 3":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[2].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 4":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[3].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		if who.name == "Police 5":
			a = analysis.getMrxRoutes(self.graph, self.polices, self.mr_x, self.move_cls)[4].shortest()
			if len(a) == 1:
				choices = self.graph.neighbors(who.get_position())
				r = random.randint(0, len(choices)-1)
				target = choices[r]
			else:
				#print a
				#print a[0][1]
				target = a[0][1]
		
	
	move_type = self.graph[who.get_position()][target][0]['ticket']
		
	if who.tickets_cab < who.tickets_bus :
		self.graph[who.get_position()][target][0]['ticket'] = 'bus'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if  who.tickets_bus < who.tickets_cab :
		self.graph[who.get_position()][target][0]['ticket'] = 'cab'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if who.tickets_cab == who.tickets_bus :
		self.graph[who.get_position()][target][0]['ticket'] = 'cab'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if who.tickets_bus == 0 :
		self.graph[who.get_position()][target][0]['ticket'] = 'cab'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if round == 3 :
		self.graph[who.get_position()][target][0]['ticket'] = 'underground'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if round == 8 :
		self.graph[who.get_position()][target][0]['ticket'] = 'underground'
		move_type = self.graph[who.get_position()][target][0]['ticket']
	if who.tickets_bus == 0 and who.tickets_cab == 0 :
		self.graph[who.get_position()][target][0]['ticket'] = 'underground'
		move_type = self.graph[who.get_position()][target][0]['ticket']
		#print who.tickets_bus
		#print who.tickets_cab
	return self.move_cls(target, move_type)
