# Solution Validator

In this folder you find the validator used to verify the solutions for the new instances. It is possible to validate any solution with the Python (2.7) script. There is an auxiliar script that receives a folder with (many) solution files and runs through them all validating them.

There is also an script to generate the best-known solution tables presented in the *solutions/* folder. The same script also updates the current best-known solutions accordingly.

## Usage

To validate a single solution file, one can call the `val.py` script with the following command:

```sh
python val.py -s path/to/solution/file.txt -i path/to/instances/file.txt
```

The result of the above command is a string printed to the standard output stating whether the solution is valid. In case it is, the script prints the number of vehicles and the total cost of the solution as well.

To validate several solution files at once, once can call the `checker.py` script with the following command:

```sh
python checker.py -s path/to/solutions/ -i path/to/instances/
```

The parameters `path/to/solutions/` and `path/to/instances/` are directories containing all the solutions to be validated and all the instances to be used in the process. If a solution has no corresponding instance, an error will occurr (but not the other way around). The result is printed to the standard output, containing one line per instance indicating whether the solution is valid, or invalid, and a final line indicating the number of instances that are valid/invalid.

The `updater.py` script is used solely to update the result tables automatically and should not be used.
