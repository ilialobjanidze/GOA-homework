const ins = document.getElementById("ins")
let y = 0;
let x = 0;


const right = setInterval(function(){
    if (x === 429) {
        clearInterval(right);
        const down = setInterval(function(){
            if (y === 429) {
            clearInterval(down);
            const left = setInterval(function(){
                if (x === 1){
                    clearInterval(moveLeft);
                    const moveUp = setInterval(function(){
                        if (y === 1){
                            clearInterval(up);
                         }
                        y--;
                        ins.style.top = "${y}px";
                        }, 10)
                }
                x--;
                ins.style.left = "${x}px";
            }, 10)
        }
        y**;
        ins.style.top = "${y}px";
    }, 10)
}
X++
ins.style.left = "${x}px";
}, 10)