/**
    # Surrounded Regions - Trapped 'O's
    
    [link](https://leetcode.com/problems/surrounded-regions/)

    Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    For example,

        X X X X
        X O O X
        X X O X
        X O X X
        
    After running your function, the board should be:

        X X X X
        X X X X
        X X X X
        X O X X
**/

var solve = function(board) {
    // tracker for trapped Os
    var trapped = board.map(function(row){
        return (new Array(row.length)).fill(true);
    });
    var visited = board.map(function(row){
        return (new Array(row.length)).fill(false);
    });

    // check for Os on surrounding edge
    edgeCoords(board).forEach(function(coord){
        if(visited[coord[0]][coord[1]]){
            return;
        }
        var x, y;
        neighbours = [coord];
        while(neighbours.length > 0){
            
            coord = neighbours.shift();
            x = coord[0]; y = coord[1];

            // mark as visited
            if(visited[x][y]) continue;
            
            visited[x][y] = true;
            
            // if is O, mark it as not trapped
            if(board[x][y] == 'O'){
                trapped[x][y] = false;
                
                // add neighbours
                var newNeighbours = validNeighbours(board, x, y).filter(function(c){
                    return !visited[c[0]][c[1]];
                });
                neighbours = neighbours.concat(newNeighbours);
            }
        }
    });
    // set all trapped ones
    trapped.forEach(function(row, i){
        row.forEach(function(t, j){
            if (t){
                board[i][j] = 'X';
            }
        });
    });
};

function validNeighbours(board, x, y){
    return [[x - 1, y], [x + 1, y], [x, y+ 1], [x, y - 1]].filter(function(coord){
        return coord[0] >= 0 && coord[0] < board.length && coord[1] >= 0 && coord[1] < board[coord[0]].length;
    });
}

function edgeCoords(board){
    var coords = [];
    // left and right edge
    board.forEach(function(row, i){
        coords.push([i, 0]);
        coords.push([i, row.length - 1]);
    });
    
    // top and bottom edge
    board[0].forEach(function(col, i){
        coords.push([0, i]);
        coords.push([board.length-1, i]);
    });
    return coords;
}

var X = 'X';
var O = 'O';
var board = ["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"];

board = board.map(function(row){
   return row.split(""); 
});


var edges = edgeCoords(board);

console.log(board);
console.log(validNeighbours(board, 1, 1));
solve(board);
console.log(board);
