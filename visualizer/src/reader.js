/**
 * Class to read instance and solution files of pdptw-instances.
 * Stores the instance and solution in appropriate fields.
 */


class Reader{
    #reader;
    instance;
    solution;
    custom_end_function;
    #bound_instance_parser;
    #bound_solution_parser;

    constructor() {
        this.#reader = new FileReader();
        this.instance = {}
        this.solution = {}

        this.custom_end_function = {};
        this.#bound_instance_parser = this.#instance_parser.bind(this)
        this.#bound_solution_parser = this.#solution_parser.bind(this)
    }

    read_instance(file, custom_end_function) {
        this.custom_end_function = custom_end_function;
        this.#reader.onloadend = this.#bound_instance_parser
        this.#reader.readAsText(file);
    }

    read_solution(file, custom_end_function) {
        this.custom_end_function = custom_end_function;
        this.#reader.onloadend = this.#bound_solution_parser
        this.#reader.readAsText(file);
    }

    #instance_parser() {
        this.instance = new Instance();

        const elements = this.#reader.result.split('\n');
        for(let l=0;l<elements.length;l++){
            let line = elements[l]
            const tv = this.#token_and_value(line)
            const token = tv[0]

            if (token === "NAME") {
                this.instance.name = tv[1].replace(/\s+/g, '')
            } else if (token === "LOCATION") {
                this.instance.location = tv[1]
            } else if (token === "TYPE") {
                this.instance.type = tv[1]
            } else if (token === "SIZE") {
                this.instance.size = parseInt(tv[1])
            } else if (token === "CAPACITY") {
                this.instance.capacity = parseInt(tv[1])
            } else if (token === "COMMENT" || token === "DISTRIBUTION" || token === "DEPOT" || token === "ROUTE-TIME" || token === "TIME-WINDOW") {
                //ignore...
            } else if (token === "NODES") {
                l = this.#node_reader(elements, l+1)
            } else if (token === "EDGES") {
                l = this.#edge_reader(elements, l+1)
            } else if (token === "EOF") {
                break
            } else {
                //Unkown keyword token
                alert("ERROR: Unknown keyword '" + token + "' token in instance file.\nAre you sure you are trying to load a valid instance file?")
                return;
            }
        }

        this.custom_end_function()
    }

    #node_reader(elements, index){
        this.instance.nodes = []

        for(let i=0; i<this.instance.size; i++){
            let line = elements[index+i]
            let values = line.split(' ')
            let node = new Node(parseInt(values[0]), [parseFloat(values[1]), parseFloat(values[2])],
                parseInt(values[3]), [parseInt(values[4]), parseInt(values[5])], parseInt(values[6]),
                parseInt(values[7]), parseInt(values[8]))

            this.instance.all_coords.push(node.coords)
            this.instance.nodes.push(node)
        }
        return index+this.instance.size-1
    }

    #edge_reader(elements, index){
        this.instance.times = []
        for(let i=0; i<this.instance.size; i++){
            let line = elements[index+i]
            let values = line.split(' ')
            let times_i = []
            for(const vstr of values){
                times_i.push(parseInt(vstr, 10))
            }
            this.instance.times.push(times_i)
        }

        return index+this.instance.size-1
    }

    #set_route_colors( ) {
        //the list below contains 120 'distinct' colors
        const vec_colors = ["#3775b2", "#b1b945", "#45b940", "#953fbb", "#64d65f", "#396ced", "#7e54d4", "#529d21", "#da68e2", "#8dc74e", "#3447b4", "#adc341", "#4d58c9", "#d1b837", "#8d7ff3", "#82a732", "#b273e8", "#70c366", "#cc3ca3", "#3b953e", "#a13ea2", "#43b26a", "#e2428a", "#50cf92", "#e53657", "#46cad2", "#d93f23", "#4b96eb", "#e99a28", "#3360bd", "#c5992a", "#4e45a3", "#9ea133", "#766ed7", "#698318", "#7a4bae", "#bec368", "#6257b8", "#dc6521", "#5b82e5", "#cd7822", "#53a4e5", "#ac3a18", "#5fc7f2", "#e84c4b", "#18a7c8", "#b82b2f", "#60caae", "#d63864", "#228758", "#e17bdc", "#30752d", "#e670b4", "#507522", "#9b6dc7", "#4b600e", "#cf93e5", "#7c7f29", "#5e4393", "#8fbb75", "#7155a7", "#9ba454", "#505099", "#d8b062", "#3c5da0", "#ef7048", "#2c7ea9", "#a55a12", "#a492e5", "#616117", "#b765ad", "#6a934c", "#93448a", "#51a177", "#ab316c", "#235e31", "#dd94c7", "#415a1f", "#a8a7e7", "#e0934e", "#6f64a6", "#b39042", "#704889", "#b2b076", "#9679bd", "#725f1a", "#7081c0", "#a8742f", "#66a1d0", "#ce5742", "#2c9d98", "#a9394c", "#3d7748", "#d46783", "#1a6447", "#e77170", "#2f7b63", "#ef9069", "#505b8f", "#a7562d", "#8a5990", "#597236", "#b46f9c", "#6b6e37", "#8d476f", "#907a39", "#90425d", "#e7ad80", "#97515a", "#7d5719", "#ed93a5", "#985c26", "#f19c8f", "#814a28", "#ca7b78", "#91633b", "#d4735b", "#ba865c", "#ac514a", "#974732"]

        let c = 0
        while (c < this.solution.routes.length) {
            this.solution.routes[c].set_color(vec_colors[c%vec_colors.length])
            c += 1;
        }
    }

    #solution_parser() {

        let elements = this.#reader.result.split('\n');
        let routes = []
        let name = ""
        let reference = ""
        let date = ""
        let author = ""

        for(var l=0;l<elements.length;l++){
            let line = elements[l]
            let tv = this.#token_and_value(line)
            let token = tv[0]

            token = token.replace(/ /g,'')

            if (token === "Instancename") {
                name = tv[1].replace(/\s+/g, '')

                if(name !== this.instance.name){
                    alert("ERROR: Solution name does not correspond to instance name.\nSolution is '".concat(name).concat("' while the loaded instance has name '").concat(this.instance.name)+"'")
                    return;
                }
            } else if (token === "Authors") {
                author = tv[1]
            } else if (token === "Date") {
                date = tv[1]
            } else if (token === "Reference") {
                reference = tv[1]
            } else if (token === "Solution") {
                routes = this.#route_reader(elements, l+1)
                l = elements.length //"Solution" should be the last part anyway
            } else {
                //Unkown keyword token
                alert("ERROR: Unknown keyword '" + token + "' token in solution file.\nAre you sure the solution file is properly formatted?")
                return;
            }
        }

        this.solution = new Solution(name, reference, date, author, routes)
        this.#set_route_colors()

        this.custom_end_function()
    }

    #route_reader(elements, index){
        let routes = []

        let r = 0
        for(let i=index;i<elements.length;i++){
            let line = elements[i]
            if(line.length === 0) break
            let values = line.split(':')
            let sequence = values[1].split(' ')
            let route = new Route(r)
            let c = 0
            route.push(0, this.instance.nodes[0].coords)
            let bn = 0
            for(const sn of sequence){
                if(sn.length === 0) continue
                let n = parseInt(sn)
                c += this.instance.times[bn][n]
                bn = n
                route.push(n, this.instance.nodes[n].coords)
            }
            c += this.instance.times[bn][0]
            route.push(0, this.instance.nodes[0].coords)
            route.cost = c

            routes.push(route)
            r += 1
        }

        return routes
    }

    #token_and_value(str){
        str = str.replace(/\t/g, "")
        let els = str.split(':', 2)
        if(els.length === 1) return [str]

        return [els[0], els[1]]
    }
}