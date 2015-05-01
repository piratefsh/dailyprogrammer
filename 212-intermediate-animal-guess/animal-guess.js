// Initialize console input prompter
var prompt = require('prompt'); prompt.start();

var questions = ['Are you thinking of an animal?', 'Is it a mammal?'];

var Node = function Node(type, content){
    this.type = type;
    this.child = null;
    this.content = content;
}

Node.prototype = {
    isLeaf: function(){
        return !this.next;
    }
}

// While haven't gotten animal answer, keep asking
while(!currNode.isLeaf()){
    askQuestion(currNode.content, function(isYes){
        if(isYes){
        }
        else{
        }
    });

    currNode = currNode.child;
}

// Got animal answer, check if its correct
askQuestion(child.content, function(isYes){
    if(isYes){
        console.log('Yay! Thanks for playing.')
    }
    else{
        console.log('Oh dear, what was the right animal?');
        askForAQuestion('')
    }
})

// Asks a given question and passes err and answer to then()
function askQuestion(question, then){
    prompt.get([{
        name: 'answer',
        description: questions[0],
        message: 'Please enter Y or N',
        pattern: /^[yn]/i
    }], function(err, response){
        then(response.answer.match(/^y/i));
    });
}

function askForAQuestion(question, then){
    prompt.get([{
        name: 'question',
        description: question,
        message: 'Please enter a valid question',
        pattern: /.*\?$/i
    }], function(err, response){
        then(response.question);
    });
}

