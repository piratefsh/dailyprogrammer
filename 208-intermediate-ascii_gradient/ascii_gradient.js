// Challenge description:
// http://www.reddit.com/r/dailyprogrammer/comments/3104wu/20150401_challenge_208_intermediate_ascii/


if(process.argv.length < 5){
    console.log("Usage for radial gradient: node ascii_gradient.js <canvas size width> <canvas size width> radial,<center x>,<center y>,<radius>");
    console.log("Usage for linear gradient: node ascii_gradient.js <canvas size width> <canvas size width>linear,<start x>,<start y>,<end x>,<end y>");
    return;
}

var x = parseInt(process.argv[3]), y = parseInt(process.argv[2]), gradientArgs = process.argv[4].split(',');
var type = gradientArgs[0], args;

// Configs for gradients
if(type == "radial"){
    args = {
        centerX: gradientArgs[2],
        centerY: gradientArgs[1],
        radius: gradientArgs[3],
        colors: ['.', ',', ':', ';', 'x', 'X', '&', '@'],
        type: type
    }
}
else if(type=="linear"){
    args = {
        startX: gradientArgs[1],
        startY: gradientArgs[2],
        endX: gradientArgs[3],
        endY: gradientArgs[4],
        colors: ['.', ',', ':', ';', 'x', 'X', '&', '@'],
        type: type
    }
}
function printGrid(grid){
    for(var i = 0; i < grid.length; i++){
        for(var j = 0; j < grid[i].length; j++){
            var color = grid[i][j] || '-';

            process.stdout.write('' + color);
        }
        process.stdout.write('\n');
    }
}

function makeGradient(grid, args){
    if(args.type == "radial"){
        makeRadialGradient(grid, args);
    }
    else if(args.type == "linear"){
        makeLinearGradient(grid, args);
    }
}

function getColor(colors, distance, maxDistance){
    if(distance > maxDistance) {
        return null;
    }
    var index = Math.floor(distance / maxDistance * colors.length);
    return colors[index];
}

function findDistance(x1, y1, x2, y2){
    return Math.floor(findRawDistance(x1, y1, x2, y2));
}

function findRawDistance(x1, y1, x2, y2){
    var x = Math.pow(x2 - x1, 2);
    var y = Math.pow(y2 - y1, 2);
    return Math.sqrt(x + y);
}

function findLinearDistance(x, y, x1, y1, x2, y2){
    if(x2 == x1){
        return y - y1;
    }
    else if (y1 == y2){
        return x - x1;
    }
    else{
        return linearDistanceMethodB(x, y, x1, y1, x2, y2);    
        return linearDistanceMethodA(x, y, x1, y1, x2, y2);    
    }
}

// Alternative linear gradient method. See 'Another formula':
// https://www.wikiwand.com/en/Distance_from_a_point_to_a_line
function linearDistanceMethodB(x, y, x1, y1, x2, y2){
    var slope, constC, d;
    slope = (1.0 * (y2 - y1)) / (x2 - x1);
    constC = y1 - slope * x1;

    var left, right;

    left = Math.pow((1.0*x+slope*y - slope*constC)/(Math.pow(slope,2) + 1) - x, 2);
    right = Math.pow(slope*((x + slope * y - slope * constC)/(slope*slope + 1)) + constC - y, 2)

    d = Math.sqrt(left + right);

    var a, b, c; 
    a = d;
    c = findRawDistance(x, y, x1, y1);
    b = pythagoreanFindB(a, c);
    return b;
}

// Finds the perpendicular distance of point to line, 
// which is directly proportional to how 'dark' the color is at that point
function linearDistanceMethodA(x, y, x1, y1, x2, y2){
    var constX, constY, constC, slope;
    slope = (1.0 * (y2 - y1)) / (x2 - x1);
    constY = 1.0;
    constX = -1.0 * slope;
    constC = slope * x1 - y1;
    var pTop = Math.abs(constX * x + constY * y + constC);
    var pBottom = Math.sqrt(Math.pow(constX, 2) + Math.pow(constY, 2));
    var perpendicularDistance = (1.0 * pTop) / pBottom; 

    var a, b, c; 
    a = perpendicularDistance;
    c = findRawDistance(x, y, x1, y1);
    b = pythagoreanFindB(a, c);
    return b;
}

function pythagoreanFindB(a, c){
    var b = Math.sqrt(Math.pow(c,2) - Math.pow(a,2));
    return Math.floor(b); 
}

function makeLinearGradient(grid, args){
    var maxDistance = findDistance(args.startX, args.startY, args.endX, args.endY)/2;
    console.log(maxDistance)
    for(var i = 0; i < grid.length; i++){
        for(var j = 0; j < grid[i].length; j++){
            var d = findLinearDistance(i, j, args.endX, args.endY, args.startX, args.startY);
            var c = getColor(args.colors, d, maxDistance);
            grid[i][j] = c;
        }
    }
}

function makeRadialGradient(grid, args){
    for(var i = 0; i < grid.length; i++){
        for(var j = 0; j < grid[i].length; j++){
            var d = findDistance(i, j, args.centerX, args.centerY);
            var c = getColor(args.colors, d, args.radius);
            grid[i][j] = c;
        }
    }
}

var grid = new Array(x);
for(var i = 0; i < x; i++){
    grid[i] = new Array(y)
};


makeGradient(grid, args);
printGrid(grid);