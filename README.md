# Instances for the Pickup and Delivery Problem with Time Windows

In this repository you can find information about the PDPTW instances proposed in my Master's thesis entitled *Pickup and Delivery Problem with Time Windows: Algorithms, Instances, and Solutions* available online at (lacks citation).

The instances are based on the Open Source Vehicle Routing Instance Generator (link), which uses real addresses and travel times in their definition. Travel times are computed by the Open Source Routing Machine (link) using Open Street Maps data. Futher information can be found in the repository of the instance generator.

This repository was inspired by others in the combinatorial optimization and operations research communities, such as the TSPLib (link), the CVRPLib (link), and the SINTEF website (link), which maintains the standard instances of the PDPTW proposed by Li and Lim (2003) and their best-known solutions.

## Instance files

Information on how to obtain the 300 files containing the definiton of the instances in the set are available under the folder *instances/*

## Best-known solutions

The detailed best-known solutions for each instance are kept under the folder *solutions/*. The folder keeps tables on best-known values as well, which can be used for comparisons and analyses in future works.

## Validator

The folder *validator/* contains a Python (2.7) script to validate solutions of the new instances. In this way, it is possible to verify if new best-known solutions respect all the constraints imposed by the PDPTW.

## How to contribute new best-known solutions

Anyone can contribute with new best-known solutions for the proposed instances. All that is needed is to submit the solution files containing the new solutions (preferably validated in advance). For the structure of the solution file, please make every effort to make it in the same way as the one detailed in the *solutions/* folder. A published reference to the work that generated the solutions is very much appreciated.
