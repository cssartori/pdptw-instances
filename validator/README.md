# Solution Validator

In this folder, you will find the validator used to verify feasibility of solutions for the new instances. It is possible to validate any solution with the Python (3.0) scripts. There is an auxiliar script that receives a folder with (many) solution files and runs through them all validating them. At the end, a a report is produced.

## Usage

To validate a single solution file, one can call the `validator.py` script with the following command:

```sh
python validator.py -s path/to/solution/file.txt -i path/to/instances/file.txt
```

The result of the above command is a string printed to the standard output stating whether the solution is valid. In case it is, the script prints the number of vehicles and the total cost of the solution as well.

To validate several solution files at once, one can call the `checker.py` script with the following command:

```sh
python checker.py -s path/to/solutions/ -i path/to/instances/
```

The parameters `path/to/solutions/` and `path/to/instances/` are directories containing all the solutions to be validated and all the instances to be used in the process, respectively. If a solution has no corresponding instance, an error will occurr (but not the other way around). The result is printed to the standard output. For detailed reports, it is possible to add a *verbosity* parameter. More information is found calling the `checker.py` script with the `-h` option.

The `updater.py` script is responsible for updating the result tables automatically, and it should not be used.

## Errors

If you encounter the error 

```
ValueError: invalid literal for int() with base 10: 'txt'
```

when using `checker.py`, this likely means that the naming of your solution file is incorrect. The name of the solution file should contain the instance name, the number of vehicles used and the cost of the solution. For example, the file name `bar-n100-1.6_733.txt` is a valid one. For more information, consult the [solutions' folder](https://github.com/cssartori/pdptw-instances/tree/master/solutions).

In the case of other errors, please do send them to: cssartori `dot` inf `dot` ufrgs `dot` br

## More information

For more information about the problem description and constraints, we refer to our [original paper](https://doi.org/10.1016/j.cor.2020.105065).
