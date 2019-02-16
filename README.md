# Instances for the Pickup and Delivery Problem with Time Windows

In this repository you can find information about the PDPTW instances proposed in my Master's thesis entitled *Pickup and Delivery Problem with Time Windows: Algorithms, Instances, and Solutions* available online at (lacks citation).

The instances are based on the Open Source Vehicle Routing Instance Generator (link), which uses real addresses and travel times in their definition. Travel times are computed by the Open Source Routing Machine (link) using Open Street Maps data. Futher information can be found in the repository of the instance generator.

This repository was inspired by others in the combinatorial optimization and operations research communities, such as the [TSPLib](https://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/), the [CVRPLib](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/), and the [SINTEF TOP](https://www.sintef.no/projectweb/top/). The latter maintains the standard instances of the PDPTW proposed by Li and Lim (2003) and their best-known solutions.

## Instance files

Information on how to obtain the 300 files containing the definiton of the instances in the set are available under the folder [instances/](https://github.com/cssartori/pdptw-instances/tree/master/instances)

## Best-known solutions

The detailed best-known solution for each instance is kept under the folder [solutions/](https://github.com/cssartori/pdptw-instances/tree/master/solutions). The folder keeps tables on best-known values as well, which can be used for comparisons and analyses in future works.

## Validator

The folder [validator/](https://github.com/cssartori/pdptw-instances/tree/master/validator) contains Python (2.7) scripts to validate solutions for the instances. In this way, it is possible to verify if new best-known solutions respect all the constraints imposed by the PDPTW. The folder also contains a brief explanation about the PDPTW constraints and provides references for those interested in further information.

## How to contribute new best-known solutions

Anyone can contribute with new best-known solutions for the proposed instances. All that is needed is to submit the solution files containing the new solutions (preferably validated in advance). For the structure of the solution file, please make every effort to have it in the same way as the one detailed in the *solutions/* folder. A published reference to the work that generated the solutions is very much appreciated.

New solutions can be submitted to: cssartori `at` inf  `dot` ufrgs `dot` br
