const child = document.getElementById("child-container");

let left = 300;
let y = 300;
let direction = "left"; // Start by moving left

const moveRight = setInterval(function(){
    if(direction == "left"){
        left--;
        if(left == 0){
            direction = "top";
        }
    } else if(direction == "top"){
        y--;
        if(y == 0){
            direction = "right";
        }
    } else if(direction == "right"){
        left++;
        if(left == 300){
            direction = "bottom";
        }
    } else{
        y++;
        if(y == 300 && left == 300){
            clearInterval(moveRight);
        }
    }

    child.style.left = left + 'px';
    child.style.top = y + 'px';
}, 10);