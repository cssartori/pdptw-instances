
function Instance( ){
    this.all_coords = []
    this.nodes = []
    this.times = []
    this.name = []
    this.type = ""
    this.size = ""
    this.capacity = 0
    this.location = ""
}

function Solution(instance_name, reference, date, author, routes){
    this.instance_name = instance_name
    this.reference = reference
    this.date = date
    this.author = author

    this.routes = routes
}

function Route(id){
    this.id = id
    this.sequence = []
    this.path = []
    this.color = "#00000"
    this.cost = 0

    this.push = function(n, coord){
        this.sequence.push(n)
        this.path.push(coord)
    }

    this.set_color = function(new_color){
        this.color = new_color
    }
}


function Node(id, coords, dem, tw, dur, p, d){
    this.id = id
    this.coords = coords
    this.demand = dem
    this.time_window = tw
    this.duration = dur

    this.is_depot = false
    this.is_pickup = false
    this.is_delivery = false
    this.pair = -1

    if(p === 0 && d === 0) this.is_depot = true;
    else if(p === 0){
        this.is_pickup = true
        this.pair = d
    }else{
        this.is_delivery = true
        this.pair = p
    }

    this.marker = {}

    this.string_name = function (){
        if(this.is_pickup){
            return String("Pickup " + this.id)
        }else if(this.is_delivery){
            return String("Delivery " + this.id)
        }
        return String("Depot " + this.id)
    }

}