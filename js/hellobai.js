var name, feeling, project;
var test = true;
test = confirm("Back at it?");
while(test){
    name = prompt("who are you?");
    if (name == "") {break;}
    feeling = prompt("Hi, " + name + ", how are you?")
    if (feeling == "good"){ break;} 
    else{
        project = prompt(name + ", what are you working on?")
        test = confirm("Can i help with " + project + "?");
    }
    
}
