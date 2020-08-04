# Instances for the Pickup and Delivery Problem with Time Windows based on open data

In this repository you can find information about the PDPTW instances proposed in the article entitled *A study on the pickup and delivery problem with time windows: Matheuristics and new instances*, Computers & Operations Research (2020). The article is available online [here](https://doi.org/10.1016/j.cor.2020.105065).

The instances were generated using real-world data for addresses and travel times. For that, the tool [Open Source Vehicle Routing Instance Generator](https://github.com/cssartori/ovig) was created. Travel times are computed using the [Open Source Routing Machine](https://github.com/Project-OSRM/osrm-backend) which takes as input [OpenStreetMap](https://planet.openstreetmap.org/) data. Addresses were obtained from the [OpenAdresses](https://openaddresses.io/) project and the [Donovan and Work (2016)](https://doi.org/10.13012/J8PN93H8) dataset. Further information can be found in the repository of the instance generator and the original article.

This repository was inspired by others in the combinatorial optimization and operations research communities, such as the [TSPLib](https://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/), the [CVRPLib](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/), and the [SINTEF TOP](https://www.sintef.no/projectweb/top/). The latter maintains the standard instances of the PDPTW proposed by Li and Lim (2003) and their best-known solutions.

## Instance files

Information on how to obtain the 300 files containing the definiton of the instances in the set are available under the folder [instances/](https://github.com/cssartori/pdptw-instances/tree/master/instances).

## Best-known solutions

The detailed best-known solution for each instance is kept under the folder [solutions/](https://github.com/cssartori/pdptw-instances/tree/master/solutions). The folder keeps tables on best-known values as well, which can be used for comparisons and analyses in future works.

## Validator

The folder [validator/](https://github.com/cssartori/pdptw-instances/tree/master/validator) contains Python (3.0) scripts to validate solutions for the instances. In this way, it is possible to verify if new best-known solutions respect all the constraints imposed by the PDPTW.

## How to contribute new best-known solutions

Anyone can contribute with new best-known solutions for the proposed instances. All that is needed is to submit the file containing the new candidate solution. For the structure of the solution file, please make every effort to have it in the same way as the one detailed in the [solutions/](https://github.com/cssartori/pdptw-instances/tree/master/solutions) folder. A reference to the work that generated the solutions is very much appreciated.

New solutions can be submitted to: cssartori `at` inf  `dot` ufrgs `dot` br

## Reference in publications

When using the instances in publications, please cite

```
@article{sartori-buriol-2020,
	title = "A Study on the Pickup and Delivery Problem with Time Windows: Matheuristics and New Instances",
	author = "Carlo S. Sartori and Luciana S. Buriol",
	journal = "Computers & Operations Research",
	pages = "105065",
	year = "2020",
	issn = "0305-0548",
	doi = "https://doi.org/10.1016/j.cor.2020.105065"
}
```