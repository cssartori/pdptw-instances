import sys, os, argparse, shutil;
import copy;
from operator import itemgetter;
import checker;
import functools;

#Prepare the arguments the program shall receive
def __prepareargs__():
	parser = argparse.ArgumentParser(description='Validade new solution files and update table information accordingly for PDPTW instances.')
	parser.add_argument('-s', nargs=1, type=str, help='Directory with new solutions', required=True)
	parser.add_argument('-i', nargs=1, type=str, help='Directory with instance files', required=True)
	parser.add_argument('-r', nargs=1, type=str, help='Reference that generated the solutions', required=True)
	parser.add_argument('-d', nargs=1, type=str, help='Submission date of solution files', required=True)
	parser.add_argument('-b', nargs=1, type=str, help='File with best-known values', required=False, default="bks.dat")
	parser.add_argument('-c', nargs=1, type=str, help='Directory with current best-known solution files', required=False, default="../solutions/files/")
	parser.add_argument('--verbose', dest='verbose', action='store_true', help='Whether to print some information', required=False)
	parser.set_defaults(verbose=False)

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
			bks[cl[0]] = [cl[0], int(cl[1]), int(cl[2]), int(cl[3]), cl[4], cl[5][:-1]]
			
	return bks

def write_bks_file(bks_filename, nbks):
	##TODO: order by size
	with open(bks_filename, "w") as f:
		text = "instance;size;vehicles;cost;reference;date\n"
		for i in nbks:
			sol = nbks[i]
			text = "%s%s;%d;%d;%d;%s;%s\n" % (text, sol[0], sol[1], sol[2], sol[3], sol[4], sol[5])

		f.write(text)

def write_solution_tables(nbks):
	def comp_inst(in1, in2):
		s1 = int(in1.split("-")[1][1:])
		s2 = int(in2.split("-")[1][1:])
		c1 = in1[0:2]
		c2 = in2[0:2]
		i1 = int(in1[-1:])
		i2 = int(in2[-1:])
		if s1 < s2:
			return -1
		elif s1 > s2:
			return 1
		elif c1 < c2:
			return -1
		elif c1 > c2:
			return 1
		elif i1 < i2:
			return -1
		elif i1 > i2:
			return 1
		else:
			return 0
	
	text = ("# Best-known solutions\n\n"
		"Here you can find the best known solutions (BKS) for the PDPTW instances in this repository. The tables below group solutions  according to the instance size (total number of locations). There are 12 sizes: 100, 200, 400, 600, 800, 1000, 1500, 2000, 2500, 3000, 4000, and 5000 locations. Each group has exactly 25 instances.\n\n"
		"For each solution, there is an available file (you may inspect the file by clicking the link). The tables present the name of the instance, the number of vehicles and cost in the current BKS solution, a reference that found the solution, and the date it was submitted.\n\n"
	)

	keylist = list(nbks.keys())
	keylist.sort(key=functools.cmp_to_key(comp_inst))
	for size in [100,200,400,600,800,1000,1500,2000,2500,3000,4000,5000]:
		tabstr = ("<details><summary>%d locations</summary>\n<p>\n\n"
				  "Instance | Vehicles | Cost | Reference | Date\n"
				  ":------: | -------: | ---: | :-------: | ---:\n" % (size))
		for k in keylist:
			sol = nbks[k]
			if sol[1] == size:
				link = "https://github.com/cssartori/pdptw-instances/blob/master/solutions/files/%s.%d_%d.txt" % (sol[0], sol[2], sol[3])
				tabstr = "%s[%s](%s) | %d | %d | %s | %s\n" % (tabstr, sol[0], link, sol[2], sol[3], sol[4], sol[5])

		tabstr = "%s\n</p>\n</details>\n\n" % (tabstr)
		text = "%s%s" % (text, tabstr)
		

	text = ("%s\n## References\n\n"
			"ARS &nbsp; &mdash; &nbsp; Dmitriy Churilov and Alexander Galko. Advantum Routing System ([advantum.ru/route](https://advantum.ru/route)).\n\n"
			"BIG3 &nbsp; &mdash; &nbsp; Dmitriy Yampolskiy, Egor Nikolaev and Daria Savina. Smart Logistics Point by the BigThree team ([big3.ru](https://big3.ru)).\n\n"
			"CH &nbsp; &mdash; &nbsp; CUHKSZ and HWGTS. Joint unpublished work by China Huawei (HW GTS optimization Lab) and Chinese University of Hong Kong (Shenzhen, CUHKSZ).  \n\n"
			"HGIM &nbsp; &mdash; &nbsp; Alexander Yuskov (a.yuskov `at` g `dot` nsu `dot` ru), Igor Kulachenko (ink `at` math `dot` nsc `dot` ru), Yury Kochetov, Igor Vasilyev, Zhangdong, Chenjuan, Huanghaohan, Wanglongfei. TBD.\n\n"
			"HS &nbsp; &mdash; &nbsp; Gerhard Hiermann and Maximilian Schiffer. A decomposition-based approach for large-scale pickup and delivery problems [arXiv](https://arxiv.org/abs/2405.00230)\n\n"
			"R &nbsp; &mdash; &nbsp; Isaiah Reimer &nbsp; (isaiah `dot` reimer `at` rideco `dot` com) - [RideCo](https://rideco.com/)\n\n"
			"SB &nbsp; &mdash; &nbsp; Carlo Sartori and Luciana Buriol. A study on the Pickup and Delivery Problem with Time Windows: Matheuristics and new instances. Available in [COR](https://doi.org/10.1016/j.cor.2020.105065)\n\n"
			"Shobb &nbsp; &mdash; &nbsp; Shobb &nbsp; ( shobb `at` narod `dot` ru )\n\n"
			"VACS &nbsp; &mdash; &nbsp; Simen T. Vadseth, Henrik Andersson, Jean-Francois Cordeau and Magnus Stålhane. To be announced.\n\n"
			"VRt &nbsp; &mdash; &nbsp; Dmitriy Demin, Mikhail Diakov (msd `at` veeroute `dot` com), Ivan Ilin, Nikita Ivanov, Viacheslav Sokolov (vs `at` veeroute `dot` com) et al. [VRt Global](https://veeroute.com/)\n\n"
			"## File naming and structure\n\n"
			"Be aware of the naming convention of the solution files. They should be named as\n\n"
			"```\n"
			"<instance-name>.<num-vehicles>_<cost>.txt\n"
			"```\n\n"
			"where `<instance-name` is the name of the instance this solution refers to, `<num-vehicles>` is the number of vehicles (or routes) in the solution and `<cost>` is the cost (or total distance/time) of this solution with no decimal places given that cost values are always integers for these instances.\n\n"
			"In terms of structure, all of the solution files are structured in a common way. We have opted to use the default format from SINTEF's website for the PDPTW and VRPTW instances that SINTEF maintains. The file [sample.txt](https://github.com/cssartori/pdptw-instances/blob/master/solutions/sample.txt) contains a sample description of a solution file. However, one can also inspect the solution files to verify their strucutre. Note that the depot is not included in the routes. Additionally, no time or load information is explicitly included, only the sequence of visits for each route.\n"
		% (text))

	with open("../solutions/README.md", "w") as f:
		f.write(text)

def update_solution_files(dir_cur_sol, dir_new_sol, obks, nbks):
	for inst in nbks.keys():
		if( obks[inst][2] == nbks[inst][2] and obks[inst][3] == nbks[inst][3]):
			continue

		os.remove(dir_cur_sol+("%s.%d_%d.txt" % (inst, obks[inst][2], obks[inst][3])))
		shutil.copy(dir_new_sol+("%s.%d_%d.txt" % (inst, nbks[inst][2], nbks[inst][3])), dir_cur_sol)


if __name__ == '__main__':
	## receive and prepare the arguments
	parser = __prepareargs__()
	args = __getargs__(parser)

	print("Reading parameters...")

    ## read parameters
	dir_new_sol = args['s'][0] ## directory with new solutions
	dir_instances = args['i'][0] ## directory with the instances of the problem
	reference = args['r'][0] ## reference
	date = args['d'][0] ## date
	bks_filename = args['b'][0] ## filename containing current BKV results
	dir_cur_sol = args['c'][0] ## directory containing current BKS
	verbose = args['verbose']

	print("Validating solutions in %s" % (dir_new_sol))
	valsol,logstr,cinv = checker.check_solutions(dir_instances, dir_new_sol, verbose)

	if cinv > 0:
		print("WARNING: There are %d invalid solutions" % (cinv))
		logstr = "%sWARNING: There are %d invalid solutions\n" % (logstr, cinv)
	else:
		logstr = "%sAll %d instances are good!\n" % (logstr,len(valsol))
		if verbose:
			print("All %d instances are good!" % (len(valsol)))

	print("Reading BKS file %s" % (bks_filename))
	bks = read_bks_file(bks_filename)
	nbks = copy.deepcopy(bks)

	improves = 0
	ties = 0
	for i in valsol.keys():
		if not i in bks:
			print("Instance %s not in BKS data. Something really wrong has happened.\nAborting opertaion..." % (i))
			sys.exit(-1)

		if ((valsol[i][0] < bks[i][2]) or (valsol[i][0] == bks[i][2] and valsol[i][1] < bks[i][3])):
			nbks[i][2] = valsol[i][0]
			nbks[i][3] = valsol[i][1]
			nbks[i][4] = reference
			nbks[i][5] = date
			improves += 1
			logstr = "%sImproved..........%s\n" % (logstr, i)
			if verbose:
				print("Improved..........%s" % (i))
		elif (valsol[i][0] == bks[i][2] and valsol[i][1] == bks[i][3]):
			ties += 1
			logstr = "%sTie...............%s\n" % (logstr, i)
			if verbose:
				print("Tie...............%s\n" % (i))
		else:
			logstr = "%sWORSE.............%s\n" % (logstr, i)
			if verbose:
				print("WORSE.............%s\n" % (i))

	if improves > 0:
		print("A total of %d solutions were improved" % (improves))
	else:
		print("WARNING: No solution improved. Did something go wrong?")

	logstr = "%sThere were %d improvements, %d ties, and %d worse solutions\n" % (logstr, improves, ties, len(valsol)-(improves+ties))

	if improves > 0:
		print("Moving new solution files from %s to %s" % (dir_new_sol, dir_cur_sol))
		update_solution_files(dir_cur_sol, dir_new_sol, bks, nbks)
		print("Writing updated BKS file %s" % (bks_filename))
		write_bks_file(bks_filename, nbks)
		print("Writing solution tables")
		write_solution_tables(nbks)

	with open("log.txt", "w") as f:
		f.write(logstr)


