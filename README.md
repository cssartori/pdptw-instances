# Instances for the Pickup and Delivery Problem with Time Windows based on open data

In this repository you can find information about the PDPTW instances proposed in the article *A study on the pickup and delivery problem with time windows: Matheuristics and new instances*, Computers & Operations Research (2020). The article is available online [here](https://doi.org/10.1016/j.cor.2020.105065).

The instances were generated using real-world data for addresses and travel times. The tool [Open Source Vehicle Routing Instance Generator](https://github.com/cssartori/ovig) was developed specifically for the purpose of generating these instances. Travel times are computed using the [Open Source Routing Machine](https://github.com/Project-OSRM/osrm-backend) which takes as input [OpenStreetMap](https://planet.openstreetmap.org/) data. Addresses were obtained from the [OpenAdresses](https://openaddresses.io/) project and the [Donovan and Work (2016)](https://doi.org/10.13012/J8PN93H8) dataset. Further information can be found in the repository of the instance generator and the original article.

This repository draws inspiration from others in the operations research community, such as the [TSPLib](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/), the [CVRPLib](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/), and [SINTEF TOP](https://www.sintef.no/projectweb/top/). The latter maintains standard instances of the PDPTW proposed by Li and Lim (2003) and their best known solutions.

## Instance files

One can find instructions on how to download the 300 instance files under the folder [instances/](https://github.com/cssartori/pdptw-instances/tree/master/instances).

## Best known solutions

The folder [solutions/](https://github.com/cssartori/pdptw-instances/tree/master/solutions) maintains information concerning the best known solutions for each instance. The folder also keeps tables with up-to-date values, which can be used for comparisons and analyses in future works.

## Validator

The folder [validator/](https://github.com/cssartori/pdptw-instances/tree/master/validator) contains Python (3.0) scripts to validate new solutions. Hence, one can verify in advance whether a new solution respects all the constraints imposed by the PDPTW and the associated instance.

## Visualizer

An instance and solution visualizer tool is available in the folder [visualizer/](https://github.com/cssartori/pdptw-instances/tree/master/visualizer). This visualization tool is implemented in Javascript and uses [Leaflet](https://leafletjs.com/) to render the real-world map and location plotting. More information can be obtained in [visualizer/](https://github.com/cssartori/pdptw-instances/tree/master/visualizer). 

## How to contribute new best known solutions

Anyone can contribute with new best known solutions for the proposed instances. All that is needed is to submit the file containing the new candidate solution. For the structure of the solution file, please make every effort to have it in the same way as the one detailed in the folder [solutions/](https://github.com/cssartori/pdptw-instances/tree/master/solutions). A reference to the work that generated the solutions is very much appreciated.

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
