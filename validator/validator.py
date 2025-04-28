import sys, os, argparse;
from operator import itemgetter
import math;
import re;

class Node:
	def __init__(self):
		self.idx = 0 ## node index
		self.etw = 0 ## time window [etw, ltw]
		self.ltw = 0
		self.dur = 0 ## service duration
		self.dem = 0 ## node demand
		self.pair = 0 ## node pair

class Instance:
	def __init__(self):
		self.size = 0 ## number of nodes
		self.capacity = 0 ## vehicle capacity
		self.nodes = list()
		self.times = list()

	def read_from_file(self, filename):	
		with open(filename, "r") as f:
			## Read HEADER section (basic information)
			for x in range(0,20):
				line = f.readline()
				fields = line.split(" ")
				
				## check which field was read
				if len(fields) == 1 and fields[0][:-1] == "NODES":
					## If reached NODES go to read section 
					break
				elif fields[0][:-1] == "SIZE":
					self.size = int(fields[1][:-1])
				elif fields[0][:-1] == "CAPACITY":
					self.capacity = int(fields[1][:-1])

			## Read NODES section
			for x in range(0, self.size):
				line = f.readline()
				fields = line.split(" ")
				
				node = Node()
				node.idx = int(fields[0])
				## ignoring latitude and longitude fields
				node.dem = int(fields[3])
				node.etw = int(fields[4])
				node.ltw = int(fields[5])
				node.dur = int(fields[6])
				
				## a node's pair is always ID+(Size/2)
				if node.dem > 0:
					node.pair = node.idx+int(math.floor(self.size/2))
				elif node.dem < 0:
					node.pair = node.idx-int(math.floor(self.size/2))
					
				self.nodes.append(node)

			## read EDGES section, which comes right after NODES
			dummy = f.readline() ## to read past "EDGES" title
			for x in range(0, self.size):
				line = f.readline()
				fields = line.split(" ")
				
				self.times.append([])
				for y in fields:
					self.times[-1].append(int(y))

					
class Solution:
	def __init__(self):
		self.inst_name = ""
		self.cost = 0
		self.routes = list()

	def read_from_file(self, filename):
		with open(filename,"r", errors='ignore') as f:
			self.cost = 0
			self.routes = list()
			
			## read past HEADER information
			for x in range(0,5):
				line = f.readline()
				cl = line.split(" : ")
				if cl[0] == "Instance name":
					self.inst_name = cl[1][:-1]

			for line in f:
				## read each route and get sequence of nodes
				sequence = line.split(":")[1]
				sequence = sequence.split(" ")
				sequence = filter(bool, sequence)
				
				## append depot as first node
				self.routes.append([0])
				
				## go through each node in sequence
				for n in sequence:
					n = re.sub(r"[\n\t\s]*", "", n)
					if n == "":
						continue   
					a = int(n)
					self.routes[-1].append(a)
					
				## append depot as last node
				self.routes[-1].append(0)

###############################################################
#### The function below is the important part in this code ####
###############################################################

def validate_solution(inst, sol):
	visited = [0 for x in range(0,inst.size)]

	## default initial values
	result = True
	cost = 0
	message = "Valid"
	
	for r in sol.routes:
		time = 0
		load = 0
		n = 0
				
		for a in r[1:]:
			if a != 0 and visited[a] == 1:
				message = "Node %d visited twice" % (a)
				result = False
				break
			
			time += inst.times[n][a]
			time = max(time, inst.nodes[a].etw)
			if time > inst.nodes[a].ltw: ## above maximum time limit of TW
				message = "Visit after time window limit at %d: %d > %d" % (a, time, inst.nodes[a].ltw)
				result = False
				break
			if inst.nodes[a].dem < 0 and visited[inst.nodes[a].pair] == 0: ## trying to deliver before pickup
				message = "Delivery before pickup for pair (%d,%d)" % (inst.nodes[a].pair, a)
				result = False
				break
			
			load += inst.nodes[a].dem
			if load > inst.capacity: ## out of vehicle capacity limits
				message = "Vehicle overloaded at %d: %d > %d" % (a, load, inst.capacity)
				result = False
				break

			## update basic values
			time += inst.nodes[a].dur
			cost += inst.times[n][a]
			n = a
			visited[a] = 1

		if not result:
			break
		
	## check if all locations were visited
	if result and sum(visited) < inst.size:
		missing = list()
		for a in range(1,len(inst.nodes)):
			if visited[a] == 0:
				missing.append(a)
				
		message = "Nodes were not visited (%d out of %d): %s" % (inst.size - sum(visited), inst.size, str(missing))
		result = False

	return [result, message,  len(sol.routes), cost]



## function just for basic setup
def validate(inst_path, sol_path):
	inst = Instance()
	inst.read_from_file(inst_path)
	sol = Solution()
	sol.read_from_file(sol_path)

	return validate_solution(inst, sol)
	

################################################################
##### The code below is for direct calling in command line #####
################################################################

## Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Validator of PDPTW solutions.')
	parser.add_argument('-i', nargs=1, type=str, help='Instance file', required=True)
	parser.add_argument('-s', nargs=1, type=str, help='Solution file', required=True)
    
	return parser

## Parse the input arguments and returns a dictionary with them
def __getargs__(parser):
	args = vars(parser.parse_args())
	return args


## procedure to call when script is used directly from command line
if __name__ == '__main__':
	## receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)

	## get parameters
	inst_path = args['i'][0] # instance filename
	sol_path = args['s'][0] # solution filename

	
	## call the main code to validate
	[valid, msg, numv, cost] = validate(inst_path, sol_path)

	## final printing of resulting operations
	if valid:
		print("Vehicles: %d  ,  Cost: %d" % (numv, cost))
	else:
		print("Error: %s" % (msg))

	## final message
	print("%s" % ("VALID" if valid else "INVALID"))

    

