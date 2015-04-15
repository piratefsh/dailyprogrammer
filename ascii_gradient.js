var x = parseInt(process.argv[3]), y = parseInt(process.argv[2]), gradientArgs = process.argv[4].split(',');
var type = gradientArgs[0], args;
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
        startX: gradientArgs[2],
        startY: gradientArgs[1],
        endX: gradientArgs[4],
        endY: gradientArgs[3],
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

function linearDistanceMethodB(x, y, x1, y1, x2, y2){
    var slope, constC, d;
    slope = (1.0 * (y2 - y1)) / (x2 - x1);
    constC = y1 - slope * x1;

    var left, right;

    left = Math.pow((1.0*x+slope*y - slope*constC)/(Math.pow(slope,2) + 1) - x, 2);
    right = Math.pow(slope*((x + slope * y - slope * constC)/(slope*slope + 1)) + constC - y, 2)

    d = Math.sqrt(left + right);
    return d;
}

function linearDistanceMethodA(x, y, x1, y1, x2, y2){
    // perpendicular distance of point to line
    // https://www.wikiwand.com/en/Distance_from_a_point_to_a_line
    var constX, constY, constC, slope;
    slope = (1.0 * (y2 - y1)) / (x2 - x1);
    constY = 1.0;
    constX = -1.0 * slope;
    constC = slope * x1 - y1;
    var pTop = Math.abs(constX * x + constY * y + constC);
    var pBottom = Math.sqrt(Math.pow(constX, 2) + Math.pow(constY, 2));
    var perpendicularDistance = (1.0 * pTop) / pBottom; 

    //pythagorean to find distance of perpendicular line intersection with gradient line
    var a, b, c; 
    a = perpendicularDistance;
    c = findRawDistance(x, y, x1, y1);
    
    b = Math.sqrt(Math.pow(c,2) - Math.pow(a,2));
   return Math.floor(b); 
}

function makeLinearGradient(grid, args){
    var maxDistance = findDistance(args.startX, args.startY, args.endX, args.endY);
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