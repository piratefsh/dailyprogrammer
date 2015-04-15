var x = parseInt(process.argv[2]), y = parseInt(process.argv[3]), gradientArgs = process.argv[4].split(',');
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

            process.stdout.write(' ' + color);
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
    if(distance > maxDistance || distance < 0) {
        return null;
    }
    var index = Math.floor(distance / maxDistance * colors.length);
    return colors[index];
}

function findDistance(x1, y1, x2, y2){
    var x = Math.pow(x2 - x1, 2);
    var y = Math.pow(y2 - y1, 2);
    return Math.floor(Math.pow((x + y), 0.5));
}

function findLinearDistance(x, y, x1, y1, x2, y2){
    var constX, constY, constC, slope;
    slope = 1.0 * (y2 - y1) / (x2 - x1);
    constY = 1.0;
    constX = -1.0 * slope;
    constC = y1 - slope*x1;
    var perpendicularDistance = Math.abs(constX * x + constY * y + constC) / Math.pow(Math.pow(constX, 2) + Math.pow(constY/2),0.5);
    // return Math.floor(Math.abs((x1-x)/2 + (y1-y)/2));
    return perpendicularDistance; 
}

function makeLinearGradient(grid, args){
    var maxDistance = Math.abs(findLinearDistance(args.startX, args.startY, args.endX, args.endY));
    for(var i = 0; i < grid.length; i++){
        for(var j = 0; j < grid[i].length; j++){
            var d = findLinearDistance(i, j, args.startX, args.startY, args.endX, args.endY);
            var c = getColor(args.colors, d, maxDistance);
            console.log(d + ', ' + maxDistance)
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