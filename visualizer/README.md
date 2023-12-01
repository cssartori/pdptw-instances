# PDPTW visualizer

This visualization tool is implemented in Javascript and employs [Leaflet](https://leafletjs.com/) for all of the map rendering tasks. You can load any instance file from this dataset as well as any associated solution file.

To start using the `visualizer`, it suffices to open the file `visualizer.html` in your preferred web browser. For now, it has been tried in both Google Chrome and Mozilla Firefox.

After loading an instance file, one can inspect the positioning of the locations, the pickup-delivery pairs, their demands and time windows. Once an associated solution file is loaded, one can also verify the routes, their costs and their visiting sequences.

#### Legend
 - Black square: the depot where routes start and end
 - Red circle: pickup location
 - Blue triangle: delivery location

#### Notes
 - This tool only supports instance and solution files that follow the formatting defined in this repository (i.e., it is not possible to visualize Li & Lim (2001) instances).
 - There may still be cases where visualization is difficult due to the sheer amount of information (many locations or routes). Suggestions on improvements are welcome.
 - Due to the map rendering, the tool may underperform for instances with 1,500+ locations. Currently, the suggestion is to use the `visualizer` for smaller instances only.

## Errors and bugs

Just like in other parts of this repository, if you find bugs or errors in the `visualizer`, please do send them to: cssartori `dot` inf `dot` ufrgs `dot` br
