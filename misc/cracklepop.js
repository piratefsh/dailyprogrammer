// Write a program that prints out the numbers 1 to 100 (inclusive). 
// If the number is divisible by 3, print Crackle instead of the number. 
// If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. 

for(var i = 1; i <= 100; i++){
    // if divisible by 3, print Crackle
    if(i % 3 == 0){
         process.stdout.write('Crackle');
    }
    // if divisible by 5, print Pop (on same line)
    if(i % 5 == 0){
         process.stdout.write('Pop');
    }
    // If neither divisible by either 3 or 5, print number
    if(i % 3 != 0 && i % 5 !=0){
        process.stdout.write(""+i);
    }
    process.stdout.write('\n');
 }

