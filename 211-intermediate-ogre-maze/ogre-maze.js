var filename = process.argv[2];
var fs = require('fs');

var maze = [];
var visited = [];
var path = [];

var money = {x: '0', y: '0'};
var ogre = {
    x: '0', 
    y: '0',
    isTouching: function(x, y){
        if(this.x == x && this.y == y){
            return true;
        }
    }
};

var data = fs.readFile(filename, function(err, data){
    if(!err && data){
        var stringMaze = String(data).split('\n');
        var row, arrRow, cell;
        for(var i = 0; i < stringMaze.length; i++){
            row = stringMaze[i].trim().split("");
            arrRow = [];
            for(var j = 0; j < row.length; j++){
                cell = row[j];
                arrRow.push(cell);
                if(cell == '@'){
                    ogre.x = i;
                    ogre.y = j;
                }
                else if(cell == '$'){
                    money.x = i;
                    money.y = j;
                }
            }
            visited.push(new Array(row.length))
            path.push(new Array(row.length))
            maze.push(arrRow);
        }
        solveMaze(ogre.x, ogre.y);
        printMaze();
    }
});

function solveMaze(x, y){
    // Reached goal
    if(x == money.x && y == money.y){
        console.log('found')
        return true;
    }

    // Has been explored or cannot be explored
    if(visited[x][y] || isWall(x, y)){
        return false;
    }

    visited[x][y] = true;

    // Go left
    if(y > 0){
        if(solveMaze(x, y - 1)){
            return isPath(x, y);
        }
    }
    // Go right
    if(y < maze[0].length -1){
        if(solveMaze(x, y + 1)){
            return isPath(x, y);
        }
    }
    // Go top
    if(x != 0){
        if(solveMaze(x - 1, y)){
            return isPath(x, y);
        }
    }
    // Go bottom
    if(x < maze.length - 1 ){
        if(solveMaze(x + 1, y)){
            return isPath(x, y);
        }
    }
    return false;
}

function isPath(x, y){
    path[x][y] = true;
    printMaze();
    return true;
}

function isWall(x, y){
    return maze[x][y] == 'O';
}

function printMaze(){
    console.log();
    for(var i = 0; i < maze.length; i++){
        for(var j = 0; j < maze[i].length; j++){
            if(path[i][j]){
                process.stdout.write('&');
            }
            else{
                process.stdout.write(maze[i][j]);
            }
        }
        process.stdout.write('\n');
    }
}
