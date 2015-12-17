function processData(input) {
    input = "" + input;
    // get salaries and queries (filter invalid ints)
    var _lines = input.split(/\r*\n/)
        .map(function(e) {
            return parseInt(e);
        })
        .filter(function(e) {
            return !isNaN(e)
        }),
        n_employees = _lines[0];
    var salaries = _lines.slice(1, n_employees + 1).sort(function(a, b) {
        return a - b;
    });
    var queries = _lines.slice(n_employees + 2);

    // console.log(salaries); return;
    for (var q of queries) {
        console.log(query(salaries, q) + 1);
    }
}


// given sorted salaries and query, return number of salaries
// such that s < query
function query(salaries, q) {
    var hi = salaries.length - 1;
    var lo = 0;

    var mid, curr, next;

    // if all salaries are lower or higher
    if (salaries[hi] <= q) {
        return hi;
    }
    else if (salaries[lo] >= q) {
        return lo - 1;
    }

    while (hi > lo && (lo >= 0 && hi < salaries.length)) {

        //search for first element >= query
        mid = parseInt((hi + lo) / 2);
        curr = salaries[mid];
        next = salaries[mid + 1];

        // found boundary
        if (curr < q && next >= q) {
            return mid;
        }
        else if (curr < q) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
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