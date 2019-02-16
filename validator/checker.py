import sys, os, argparse;
from operator import itemgetter;
import val;

#Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Parse result files and logs grouping information in a new file')
	parser.add_argument('-s', nargs=1, type=str, help='Directory with new solutions', required=True)
	parser.add_argument('-i', nargs=1, type=str, help='Directory with instance files', required=True)
    
	return parser

#Parse the input arguments and returns a dictionary with them
def __getargs__(parser):
	args = vars(parser.parse_args())
	return args

# Get all files (recursively) under folder direc ending with ext(ension)
def get_list_of_files(direc, ext=""):
	files = list() ## a list of all files
	dir_list = os.listdir(direc)

	for a in dir_list:
		path = os.path.join(direc, a)
		if os.path.isdir(path): ## check if it is a directory
			## call the function in the directory to get its files
			files += get_list_of_files(path, ext)
		elif not ext or a.endswith(ext):
			files.append(path)
		
	return files


def check_solutions(dir_instances, dir_new_sol):

	logstr = "" ## log
	vs = dict() ## set with valid solutions
	cinvalid = 0 ## counter of invalid solutions
	for filename in get_list_of_files(dir_new_sol, ".txt"):
		inst = filename.split("/")[-1].split(".")[0]
		iname = inst
		sz = inst.split("-")[1][1:]
		inst = dir_instances + ("n%s/" % (sz)) + inst + ".txt"

		rveh = int(filename.split("/")[-1].split(".")[1].split("_")[0]) ## reported vehicles
		rcst = int(filename.split("/")[-1].split(".")[1].split("_")[1]) ## reported cost
		
		c = val.validate(inst, filename)
		if c[0] == 0:
			cinvalid += 1
			logstr = "%sINF...............%s\n" % (logstr, filename)
		else:
			logstr = "%sOK................%s\n" % (logstr, filename)
			if c[1] != rveh or c[2] != rcst:
				logstr = "%s...Disagreement...%s\n" % (logstr, filename)
			vs[iname] = [c[1], c[2]]

	return vs,logstr,cinvalid


if __name__ == '__main__':
	## receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)

    ## read parameters
	dir_new_sol = args['s'][0] ## directory with new solutions
	dir_instances = args['i'][0] ## directory with the instances of the problem
	
	print "Validating..."
	valsol,logstr,cinv = check_solutions(dir_instances, dir_new_sol)
	if cinv > 0:
		print "There are %d invalid solutions out of %d" % (cinv, cinv+len(valsol))
	else:
		print "All %d instances are good!" % (len(valsol))
	# with open("log.txt", "w") as f:
	# 	f.write(logstr)

	
