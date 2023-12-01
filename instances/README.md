# Instance files

There are 300 instance files in total. They are distributed among 12 size groups: 100, 200, 400, 600, 800, 1000, 1500, 2000, 2500, 3000, 4000, and 5000 locations. Each group contains exactly 25 instances located in four cities (Barcelona, Berlin, New York, and Porto Alegre) with a wide range of configurations.

The 300 instance files are too large to be stored in this git repository due to the complete travel time matrix they hold in each file. Hence, this README keeps a reference link to download all the files.

## Download

The instances have an official dataset in Mendeley Data, which has a permanent link. All the instance files can be downloaded from:

https://data.mendeley.com/datasets/wr2ct4r22f/2

## File description

Each compressed (.zip) file contains one group of instances and a descriptive README file explaining how the instances should be read, and the information provided in each section of the file. The same description is presented here in the file [how_to_read.txt](https://github.com/cssartori/pdptw-instances/blob/master/instances/how_to_read.txt)

## Configurations of the instances

There is a text file [configurations.txt](https://github.com/cssartori/pdptw-instances/blob/master/instances/configurations.txt) in this folder, which contains the characteristics for each one of the 300 instances. The configurations include the distribution of locations used for each instance, the city it was generated in, number of clusters and their density (if appropriate), time window width, scheduling horizon, service durations, vehicle capacities, and position of the depot.

For more information on how the instances were generated, one is referred to our [original paper](https://doi.org/10.1016/j.cor.2020.105065) and to the repository of the [instance generator](https://github.com/cssartori/ovig/).
