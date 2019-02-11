import sys, os, argparse, shutil;
import copy;
from operator import itemgetter;
import checker;

#Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Parse result files and logs grouping information in a new file')
	parser.add_argument('-s', nargs=1, type=str, help='Directory with new solutions', required=True)
	parser.add_argument('-i', nargs=1, type=str, help='Directory with instance files', required=True)
	parser.add_argument('-r', nargs=1, type=str, help='Reference that generated the solutions', required=True)
	parser.add_argument('-d', nargs=1, type=str, help='Solultions\' submission date', required=True)
	parser.add_argument('-b', nargs=1, type=str, help='File with best-known values', required=False, default="newbks.dat")
	parser.add_argument('-c', nargs=1, type=str, help='Directory with current best-known solution files', required=False, default="solbks")
    
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

def read_bks_file(bks_filename):
	bks = dict()
	with open(bks_filename, "r") as f:
		h = f.readline()
		for line in f:
			cl = line.split(";")
			bks[cl[0]] = [cl[0], int(cl[1]), int(cl[2]), int(cl[3]), cl[4], cl[5]]
			
	return bks

def write_bks_file(bks_filename, nbks):
	with open(bks_filename, "w") as f:
		for sol in nbks:
			f.write("%s;%d;%d;%d;%s;%s" % (sol[0], sol[1], sol[2], sol[3], sol[4], sol[5]))


def write_solution_tables(nbks):
	text = ("# Best-known solutions\n\n"
	 "Here you can find the best-known solutions (BKS) for the PDPTW instances. Below, the solutions are grouped according to the instance size "
	 "(number of locations). There are 12 sizes: 100, 200, 400, 600, 800, 1000, 1500, 2000, 2500, 3000, 4000, and 5000 locations. Each group has "
	 "exactly 25 instances.\n\n"
	 "For each solution, there is a detailed solution file available. In the following tables, it is presented the name of the instance, the number "
	 "of vehicles and cost in the current BKS solution, a reference that found the solution, and the date it was submitted.\n\n")

	for size in [100,200,400,600,800,1000,1500,2000,2500,3000,4000,5000]:
		tabstr = ("<details><summary>%d locations</summary>\n<p>\n\n"
				  "Instance | Vehicles | Cost | Reference | Date"
				  ":------: | -------: | ---: | :-------: | ---:\n" % (size))
		for sol in nbks:
			if sol[1] == size:
				tabstr = "%s%s | %d | %d | %s | %s\n" % (tabstr, sol[0], sol[2], sol[3], sol[4], sol[5])

		tabstr = "%s\n</p>\n</details>\n\n" % (tabstr)
		text = "%s%s" % (text, tabstr)
		

	text = ("%s\n## References\n\n"
			"TODO: add reference\n\n"
			"## File structure\n\n"
			"All instance files are structured in a common way. It follows the default format of SINTEF website for the PDPTW instances maintained by them. "
			"Below you can find a simple description, although one can inspect the solution files to see the strucutre as well.\n\n"
			"TODO: explain\n\n" % (text))

	with open("../solutions/README.md", "w") as f:
		f.write(text)

def update_solution_files(dir_cur_sol, dir_new_sol, obks, nbks):
	for inst in nbks.keys():
		if( obks[inst][2] == nbks[inst][2] and obks[inst][3] == nbks[inst][3]):
			continue

		os.remove(dir_cur_sol+("%s.%d_%d.txt" % (inst, obks[2], obks[3])))
		shutil.copy(dir_new_sol+("%s.%d_%d.txt" % (inst, nbks[2], nbks[3])), dir_cur_sol)
	
		
if __name__ == '__main__':
	## receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)

    ## read parameters
	dir_new_sol = args['s'][0] ## directory with new solutions
	dir_instances = args['i'][0] ## directory with the instances of the problem
	reference = args['r'][0] ## reference
	date = args['d'][0] ## date
	bks_filename = args['b'][0] ## filename containing current BKV results
	dir_cur_sol = args['c'][0] ## directory containing current BKS

	valsol,logstr,cinv = checker.check_solutions(dir_instances, dir_new_sol)
	
	if cinv > 0:
		print "WARNING: There are %d invalid solutions" % (cinv)
		logstr = "%sWARNING: There are %d invalid solutions\n" % (logstr, cinv)
	else:
		logstr = "%sAll %d instances are good!\n" % (logstr,len(valsol))

	bks = read_bks_file(bks_filename)
	nbks = copy.deepcopy(bks)
	
	improves = 0
	ties = 0
	for i in valsol.keys():
		if not i in bks:
			print "Instance %s not in BKS data. Something really wrong has happened.\nAborting opertaion..." % (i)
			sys.exit(-1)

		if ((valsol[i][0] < bks[i][1]) or (valsol[i][0] == bks[i][2] and valsol[i][1] < bks[i][3])):
			nbks[i][2] = valsol[i][0]
			nbks[i][3] = valsol[i][1]
			nbks[i][4] = reference
			nbks[i][5] = date
			improves += 1
			logstr = "%sImproved..........%s\n" % (logstr, i)
		elif (valsol[i][0] == bks[i][2] and valsol[i][1] == bks[i][3]):
			ties += 1
			logstr = "%sTie...............%s\n" % (logstr, i)
		else:
			logstr = "%sWORSE.............%s\n" % (logstr, i)

	if improves > 0:
		print "A total of %d solutions were improved" % (improves)
	else:
		print "WARNING: No solution improved. Did something go wrong?"
		
	logstr = "%sThere were %d improvements, %d ties, and %d worse solutions\n" % (logstr, improves, ties, len(valsol)-(improves+ties))

	if improves > 0:
		write_bks_file(bks_filename, nbks)
		write_solution_tables(nbks)
		#update_solution_files(dir_cur_sol, dir_new_sol, bks, nbks)
	
	with open("log.txt", "w") as f:
		f.write(logstr)

	
	
