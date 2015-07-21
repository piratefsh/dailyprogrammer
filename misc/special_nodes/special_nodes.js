var util = require('util');

function processData(input) {
    //Enter your code here
    input = "" + input;
    var _lines = input.split(/\n/);

    var _n = _lines[0].split(' '),
        n_nodes = parseInt(_n[0]),
        n_edges = parseInt(_n[1]);

    var edges = _lines.slice(1, n_edges + 1);
    var special_nodes = _lines[_lines.length-1].split(' ').filter(function(e){return e && e.length > 0});

    var graph = make_graph(edges, special_nodes);

    var shortest_dists = {};
    for(var s in graph){
        // distances to specials
        var s = shortest_path(s, graph, special_nodes);
        console.log(s);
    }
}

function shortest_path(source, graph, special_nodes){
    // priority queue for unvisited nodes
    initialize_graph(graph, source);

    var Q = Object.keys(graph); 

    while(Q.length > 0){
        Q.sort(function(a, b){return graph[a].distance - graph[b].distance});

        var curr_id = Q.shift(),
            curr = graph[curr_id];
        curr.visited = true;

        if (special_nodes.indexOf(curr_id) > -1){
            return curr.distance;
        }

        for(var n in curr.neighbours){
            var neighbour = graph[n];

            if (!neighbour.visited){
                var alt_distance = curr.distance + curr.neighbours[n];
                if (alt_distance < neighbour.distance){
                    neighbour.distance = alt_distance;
                    neighbour.path.push(curr_id);
                }
            }
        }
    }

    return graph;
}

function initialize_graph(graph, source){
    // initialize all node to have empty path and max distance from src 
    for (var node in graph){
        graph[node].visited = false;
        graph[node].path = [];
        graph[node].distance = Number.MAX_VALUE;
    }
    graph[source].distance = 0;
}

function make_graph(edges, special_nodes) {
    var nodes = {};

    for (var e of edges) {
        var edge = e.split(' '),
            node = edge[0],
            neighbour = edge[1],
            weight = parseInt(edge[2]);

        add_neighbour(node, neighbour, weight, nodes, special_nodes);
        add_neighbour(neighbour, node, weight, nodes, special_nodes);
    }
    return nodes;
}

function add_neighbour(node, neighbour, weight, nodes, special_nodes) {
    if (node in nodes) {
        var ns = nodes[node].neighbours;

        if(neighbour in ns){
            var curr_weight = ns[neighbour];
            ns[neighbour] = weight < curr_weight? weight : curr_weight;
        }
        else{
            ns[neighbour] = weight;
        }
    }
    else {
        nodes[node] = {
            neighbours: {},
            visited: false,
            special: special_nodes.indexOf(node) >= 0
        }
        nodes[node].neighbours[neighbour] = weight;
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function(input) {
    _input += input;
});

process.stdin.on("end", function() {
    processData(_input);
});