import sys, os, argparse;
from operator import itemgetter;
import validator;

verbosity=0

#Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Validates all PDPTW solutions in a folder.')
	parser.add_argument('-s', nargs=1, type=str, help='Directory with new solutions', required=True)
	parser.add_argument('-i', nargs=1, type=str, help='Directory with instance files', required=True)
	parser.add_argument('-v', nargs=1, type=str, help='Verbosity leve ((less) 0,1,2,3 (more)).', required=False)
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


def check_solutions(dir_instances, dir_new_sol, verbose=False):
	global verbosity
	logstr = "" ## log
	vs = dict() ## set with valid solutions
	cinvalid = 0 ## counter of invalid solutions
	lf = get_list_of_files(dir_new_sol, ".txt")

	if verbose:
		verbosity = 2

	for filename in lf:
		inst = filename.split("/")[-1].split(".")[0]
		iname = inst
		sz = inst.split("-")[1][1:]
		inst = dir_instances + inst + ".txt"

		rveh = int(filename.split("/")[-1].split(".")[1].split("_")[0]) ## reported vehicles
		rcst = int(filename.split("/")[-1].split(".")[1].split("_")[1]) ## reported cost

		c = validator.validate(inst, filename)
		if not c[0]:
			cinvalid += 1
			logstr = "%sInvalid...............%s\n" % (logstr, filename)
			if verbosity >= 2:
				print("Invalid...............%s" % (filename))
		else:
			logstr = "%sValid.................%s\n" % (logstr, filename)
			if verbosity >= 2:
				print("Valid.................%s" % (filename))

			if c[2] != rveh or c[3] != rcst:
				logstr = "%s...Disagreement...%s\n" % (logstr, filename)
				if verbosity >= 3:
					print("\t...Disagreement...%s" % (filename))

			vs[iname] = [c[2], c[3]]

	return vs,logstr,cinvalid


if __name__ == '__main__':
	## receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)

    ## read parameters
	dir_new_sol = args['s'][0] ## directory with new solutions
	dir_instances = args['i'][0] ## directory with the instances of the problem
	verbosity = 0
	if args['v'] != None:
		verbosity = int(args['v'][0])
	if verbosity >= 1:
		print("Validating...")

	valsol,logstr,cinv = check_solutions(dir_instances, dir_new_sol)

	if verbosity >= 1:
		print("Validation log:\n%s" % (logstr))

	if cinv > 0:
		print("There are %d invalid solutions out of %d" % (cinv, cinv+len(valsol)))
	else:
		print("All %d solutions are good!" % (len(valsol)))


