var name, feeling, project;
var test;
test = confirm("Back at it?");
while(test){
    name = prompt("who are you?");
    if (name == "") {break;}
    feeling = prompt("Hi, " + name + ", how are you?")
    if (feeling == "good"){ 
        alert(name + " is feeling " + feeling + "; we are done here.")
        break;
    } 
    else{
        project = prompt(name + ", what are you working on?")
        projectHelpNeeded = confirm("Can i help with " + project + "?");
        if (projectHelpNeeded){ // TODO - rest of the code
            alert("still working on developing that capability :/!");
        } 
        test = confirm("Back at it?");      
    }
    
}
