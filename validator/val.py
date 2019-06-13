import sys, os, argparse;
from operator import itemgetter

class Node:
	def __init__(self):
		self.idx = 0
		self.setw = 0
		self.ltw = 0
		self.stw = 0
		self.dem = 0
		self.pair = 0

class Instance:
	def __init__(self):
		self.size = 0
		self.cap = 0
		self.nodes = list()
		self.times = list()

class Solution:
	def __init__(self):
		self.cost = 0
		self.routes = list()

#Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Validator of PDPTW solutions.')
	parser.add_argument('-i', nargs=1, type=str, help='Instance file', required=True)
	parser.add_argument('-s', nargs=1, type=str, help='Solution file', required=True)
	parser.add_argument('-f', nargs=1, type=str, help='Format of the instance file', required=False, default="sb")
	## TODO: add a li-lim instance reader to validate them as well
    
	return parser

#Parse the input arguments and returns a dictionary with them
def __getargs__(parser):
	args = vars(parser.parse_args())
	return args


def read_instance(filename):
	inst = Instance()
	
	with open(filename, "r") as f:
		for x in xrange(0,20):
			line = f.readline()
			cl = line.split(" ")
			if len(cl) == 1 and cl[0][:-1] == "NODES":
				break
			elif cl[0][:-1] == "SIZE":
				inst.size = int(cl[1][:-1])
			elif cl[0][:-1] == "CAPACITY":
				inst.cap = int(cl[1][:-1])

		for x in xrange(0, inst.size):
			line = f.readline()
			cl = line.split(" ")
			node = Node()
			node.idx = int(cl[0])
			node.cap = int(cl[3])
			node.etw = int(cl[4])
			node.ltw = int(cl[5])
			node.stw = int(cl[6])
			if node.cap > 0:
				node.pair = node.idx+(inst.size/2)
			elif node.cap < 0:
				node.pair = node.idx-(inst.size/2)
			inst.nodes.append(node)

		dummy = f.readline()
		for x in xrange(0,inst.size):
			line = f.readline()
			cl = line.split(" ")
			inst.times.append([])
			for y in cl:
				inst.times[-1].append(int(y))

	return inst

def read_solution(filename, inst):
	sol = Solution()
	with open(filename,"r") as f:
		for x in xrange(0,5):
			line = f.readline()

		for line in f:
			cl = line.split(":")[1]
			cl = cl.split(" ")
			cl = filter(bool,cl)
			sol.routes.append([0])
			for n in cl:
				a = int(n)
				sol.cost += inst.times[sol.routes[-1][-1]][a]
				sol.routes[-1].append(a)
				
			sol.cost += inst.times[sol.routes[-1][-1]][0]
			sol.routes[-1].append(0)
			
	return sol

def validate_solution(inst, sol):
	visited = [0 for x in xrange(0,inst.size)]
	for r in sol.routes:
		time = 0
		load = 0
		n = 0
		
		for a in r[1:]:
			#print "%d -- %d.0 --> %d" % (n, inst.times[n][a], a)
			time += inst.times[n][a]
			time = max(time, inst.nodes[a].etw)
			if time > inst.nodes[a].ltw: ## above maximum limit of TW
				print "TW %d %d" % (a, time)
				return False
			if inst.nodes[a].dem < 0 and visited[inst.nodes[a].pair] == 0: ## trying to deliver before pickup
				print "DEMAND"
				return False
			load += inst.nodes[a].dem
			if load > inst.cap: ## out of vehicle capacity limits
				print "LOAD"
				return False
			
			time += inst.nodes[a].stw
			n = a
			visited[a] = 1

	if sum(visited) < inst.size: ## not all locations visited
		print "VISITED: %d" % (sum(visited))
		return False

	return True


def validate(iname, sname):
	inst = read_instance(iname)
	sol = read_solution(sname, inst)

	## returns a list containing 3 elements: [ 0 or 1 , num. routes , total route cost]
	## if 1st element is 0: solution is invalid. Else if it is 1, solution is valid.
	return [1 if validate_solution(inst, sol) else 0, len(sol.routes), sol.cost]



if __name__ == '__main__':
	#receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)

    #read parameters
	inst_name = args['i'][0] # instance filename
	sol_name = args['s'][0] # solution filename
	fmt = args['f'] # format of the instance file

	if fmt != "sb":
		print "Unknown instance format %s" % (fmt)
		sys.exit(-1)

	inst = read_instance(inst_name)
	sol = read_solution(sol_name, inst)
	valid = validate_solution(inst, sol)
	print "%s" % ("Valid" if valid else "Invalid")
	if valid:
		print "Veh.: %d   Cost: %d" % (len(sol.routes), sol.cost)
