import sys, os, argparse, shutil;
import copy;
from operator import itemgetter;
import checker;
import functools;
from validator import Solution, Instance;
import validator;

#Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Fix solution file which do not follow the correct format.')
	parser.add_argument('-s', nargs=1, type=str, help='Directory with soltuions to fix', required=True)
	parser.add_argument('-i', nargs=1, type=str, help='Directory with instance files', required=True)
	parser.add_argument('-d', nargs=1, type=str, help='directory where to save the fixed files', required=True)
    
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



def fix_file(solfile, instdir, new_dir):
	print("File %s" % (solfile))
	sol = Solution()
	sol.read_from_file(solfile)

	instpath = instdir + sol.inst_name + ".txt"

	inst = Instance()
	inst.read_from_file(instpath)

	[result, message, num_routes, cost] = validator.validate_solution(inst, sol)

	if not result:
		print("WARNING: solution file %s is not valid" % (solfile))
	else:
		new_file_name = new_dir + sol.inst_name + (".%d_%.0f.txt" % (num_routes, cost))
		print("Fixing file %s and moving to %s" % (solfile, new_file_name))
		shutil.copy(solfile, new_file_name)



if __name__ == '__main__':
	## receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)
	
	print("Reading parameters...")
	
	## read parameters
	dir_fix_sol = args['s'][0] ## directory with solutions to be fixed
	dir_instances = args['i'][0] ## directory with the instances of the problem
	new_dir = args['d'][0] ## directory containing current BKS

	list_of_sol_files = get_list_of_files(dir_fix_sol, ".txt")
	print("Found %d solution files to fix..." % (len(list_of_sol_files)))

	for solfile in list_of_sol_files:
		fix_file(solfile, dir_instances, new_dir)


	print("DONE")
