## Instance file structure and how to read
##
## The first 10 lines of each file contain general information about the
## instance. All times are measured in minutes, whereas capacity and demands
## are measured in units of goods.
##
## The most important information is in the following fields:
##
## SIZE: <number of locations in the instance including the depot>
## ROUTE-TIME: <the maximum time vehicles must return to the depot (horizon)>
## CAPACITY: <maximum capacity of each vehicle>
##
## Next, a NODES field is followed by SIZE lines containing the complete
## information of each location in the instance file. For each line,
## there are 9 fields separated by a single space character.
##
## <id> <lat> <long> <dem> <etw> <ltw> <sd> <p> <d>
##
## <id> is the node identifier ( node 0 is the unique depot ).
## <lat> <lon> are the latitude and longitude coordinates of the location.
## <dem> is the demand ( dem > 0 for pickup, dem < 0 for delivery ).
## <etw> <ltw> are the time window [etw,ltw] of the location.
## <sd> is the service duration at that location.
## <p> is the pickup pair if <id> is a delivery, and 0 otherwise.
## <d> is the delivery pair if <id> is a pickup, and 0 otherwise.
##
## The <p> and <d> are for completeness reasons only, because the delivery of
## each pickup location <id> is given by (<id>+((SIZE-1)/2)). Analogous for
## delivery location <id> the pickup is given by (<id>-((SIZE-1)/2)).
##
## NOTE: there are only two float values in the instance: <lat> and <lon>.
##
## After the NODES, there is an EDGES field, followed by SIZE lines
## each line with SIZE integer values separated by a single space character.
## These integers are the travel times between each location in the instance,
## measured in minutes and computed throughout the OSRM tool.
##
## All instances end with an EOF field.
##
##
##
## Carlo Sartori and Luciana Buriol (2019).
