    var filename = process.argv[2];
    var fs = require('fs');

    var maze = [];
    var visited = [];
    var path = [];

    var money = {x: '0', y: '0'};
    var ogre = {
        found: false,
        x: '0', 
        y: '0',
        size: '2',
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
                    if(cell == '@' && !ogre.found){
                        ogre.x = i;
                        ogre.y = j;
                        ogre.found = true;
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
            if(solveMaze(ogre.x, ogre.y)){
                printMaze();
            }
            else{
                console.log('No path :(')
            }
        }
    });

    function isOnMoney(x, y){
        return (maze[x][y] == '$' || maze[x][y+1] == '$'
            || maze[x+1][y] == '$' || maze[x+1][y+1] == '$');
    }

    function solveMaze(x, y){
        // Reached goal
        if(isOnMoney(x, y)){
            isPath(x, y)
            return true;
        }

        // Has been explored or cannot be explored
        if(visited[x][y] || isWall(x, y)){
            return false;
        }

        visited[x][y] = true;

        // Go left
        if(canGo('left', x, y)){
            if(solveMaze(x, y - 1)){
                return isPath(x, y);
            }
        }
        // Go right
        if(canGo('right', x, y)){
            if(solveMaze(x, y + 1)){
                return isPath(x, y);
            }
        }
        // Go top
        if(canGo('top', x, y)){
            if(solveMaze(x - 1, y)){
                return isPath(x, y);
            }
        }
        // Go bottom
        if(canGo('bottom', x, y)){
            if(solveMaze(x + 1, y)){
                console.log('bottom')
                return isPath(x, y);
            }
        }
        return false;
    }

    function canGo(direction, x, y){
        var isNotEdge, isNotWall;
        switch(direction){
            case 'left':
                isNotEdge = y > 0;
                return isNotEdge && !isWall(x, y-1) && (maze[x+1] && !isWall(x+1, y-1));
            case 'right':
                isNotEdge = y < maze[0].length - 2;
                return isNotEdge && !isWall(x, y+2) && (maze[x+1] && !isWall(x+1, y+2));
            case 'top': 
                isNotEdge = x > 0;
                return isNotEdge && !isWall(x-1, y) && (maze[y+1] && !isWall(x-1, y+1));
            case 'bottom': 
                isNotEdge = x < maze.length - 2;
                return isNotEdge && !isWall(x+2, y) && (maze[y+1] && !isWall(x+2, y+1));
        }
    }

    function isPath(x, y){
        path[x][y] = true;
        return true;
    }

    function isWall(x, y){
        return maze[x][y] == 'O';
    }

    function printMaze(){
        console.log();
        for(var i = 0; i < maze.length; i++){
            for(var j = 0; j < maze[i].length; j++){
                if(path[i][j] || i != 0 && path[i - 1][j]
                    || j!=0 && path[i][j - 1] || (i!=0 && j!=0) && path[i - 1][j-1 ]){
                    process.stdout.write('&');
                }
                else{
                    process.stdout.write(maze[i][j]);
                }
            }
            process.stdout.write('\n');
        }
    }
