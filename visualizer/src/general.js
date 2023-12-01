
function startup(){
    deactivate_load_solution_button();
    reset_nodes_list()
    reset_routes_list()
}

function reset_routes_list(){
    let routes_btn = document.getElementById("routes_button")
    let routes_icon = document.getElementById("routes-icon")

    routes_icon.className = 'fa fa-angle-down';

    let routes_container = document.getElementById('routes_dropdown');
    routes_container.innerHTML = "";
    routes_container.style.display = "none";

    let routes_list_open = false;
    routes_btn.addEventListener('click', function(){
        if(routes_list_open){
            routes_icon.className = 'fa fa-angle-down';
        } else{
            routes_icon.className = 'fa fa-angle-down open';
        }

        routes_btn.blur()

        routes_list_open = !routes_list_open;
    });

    deactivate_routes_list()
}

function reset_nodes_list(){
    let nodes_btn = document.getElementById("nodes_button")
    let nodes_icon = document.getElementById("nodes-icon")

    nodes_icon.className = 'fa fa-angle-down';

    let nodes_container = document.getElementById('nodes_dropdown');
    nodes_container.innerHTML = "";
    nodes_container.style.display = "none";

    let nodes_list_open = false;
    nodes_btn.addEventListener('click', function(){
        if(nodes_list_open){
            nodes_icon.className = 'fa fa-angle-down';
        } else{
            nodes_icon.className = 'fa fa-angle-down open';
        }

        nodes_btn.blur()

        nodes_list_open = !nodes_list_open;
    });

    deactivate_nodes_list()
}

function activate_nodes_list(){
    document.getElementById("nodes_button").disabled = false;
    let nodes_btn = document.getElementById("nodes_button")


    nodes_btn.style.color = "#d3cdcd"
    nodes_btn.addEventListener("mouseenter", function( event ) {
        event.target.style.color = "#ee9d8c";
    }, false);
    nodes_btn.addEventListener("mouseleave", function( event ) {
        event.target.style.color = "#d3cdcd";
    }, false);
}

function deactivate_nodes_list(){
    document.getElementById("nodes_button").disabled = true;
    let nodes_btn = document.getElementById("nodes_button")


    nodes_btn.style.color = "#919191"
    nodes_btn.addEventListener("mouseenter", function( event ) {
        event.target.style.color = "#919191";
    }, false);
    nodes_btn.addEventListener("mouseleave", function( event ) {
        event.target.style.color = "#919191";
    }, false);
}

function activate_routes_list(){
    document.getElementById("routes_button").disabled = false;
    let routes_btn = document.getElementById("routes_button")


    routes_btn.style.color = "#d3cdcd"
    routes_btn.addEventListener("mouseenter", function( event ) {
        event.target.style.color = "#ee9d8c";
    }, false);
    routes_btn.addEventListener("mouseleave", function( event ) {
        event.target.style.color = "#d3cdcd";
    }, false);
}

function deactivate_routes_list(){
    document.getElementById("routes_button").disabled = true;
    let routes_btn = document.getElementById("routes_button")


    routes_btn.style.color = "#919191"
    routes_btn.addEventListener("mouseenter", function( event ) {
        event.target.style.color = "#919191";
    }, false);
    routes_btn.addEventListener("mouseleave", function( event ) {
        event.target.style.color = "#919191";
    }, false);
}


function activate_load_solution_button(){
    document.getElementById("load_solution").disabled = false;
    let ls_btn = document.getElementById("load_solution_btn")


    ls_btn.style.color = "#d3cdcd"
    ls_btn.addEventListener("mouseenter", function( event ) {
        event.target.style.color = "#ee9d8c";
    }, false);
    ls_btn.addEventListener("mouseleave", function( event ) {
        event.target.style.color = "#d3cdcd";
    }, false);
}

function deactivate_load_solution_button(){
    document.getElementById("load_solution").disabled = true;
    let ls_btn = document.getElementById("load_solution_btn")

    ls_btn.style.color = "#919191"
    ls_btn.addEventListener("mouseenter", function( event ) {
        event.target.style.color = "#919191";
    }, false);
    ls_btn.addEventListener("mouseleave", function( event ) {
        event.target.style.color = "#919191";
    }, false);
}

//dropdowns
click_open_close_dropdown();

function click_open_close_dropdown(){
    //hide or show content under dropdown
    /* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
    var dropdown = document.getElementsByClassName("dropdown-btn");
    var i;

    for (i = 0; i < dropdown.length; i++) {
        dropdown[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === "block") {
                dropdownContent.style.display = "none";
            } else {
                dropdownContent.style.display = "block";
            }
        });
    }
}

function close_dropdowns(){
    var dropdown = document.getElementsByClassName("dropdown-btn");
    for (i = 0; i < dropdown.length; i++){
        var dropdownContent = dropdown[i].nextElementSibling;
        if(dropdownContent.style.display === "block"){
            dropdown[i].classList.toggle("active");
            dropdownContent.style.display = "none";
        }
    }
}