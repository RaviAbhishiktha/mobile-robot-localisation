// ===================
// CO1 Agent Model
// ===================

function runCO1(){

    let robot = {
        x:0,
        y:0,
        direction:"N"
    };

    robot.y += 1;
    robot.direction = "E";
    robot.x += 1;

    document.getElementById("co1").innerHTML =
    `Robot Position = (${robot.x}, ${robot.y})
    Direction = ${robot.direction}`;
}



// ===================
// CO2 BFS Search
// ===================

function runCO2(){

    const grid = [
        [0,0,0,0],
        [1,1,0,1],
        [0,0,0,0],
        [0,1,1,0]
    ];

    const start = [0,0];
    const goal = [3,3];

    let queue = [[start,[start]]];
    let visited = new Set();

    while(queue.length){

        let [node,path] = queue.shift();

        let key = node.toString();

        if(visited.has(key))
            continue;

        visited.add(key);

        if(node[0]===goal[0] && node[1]===goal[1]){

            document.getElementById("co2").innerHTML =
            "Path: " + JSON.stringify(path);

            return;
        }

        let dirs = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ];

        for(let d of dirs){

            let nx=node[0]+d[0];
            let ny=node[1]+d[1];

            if(
                nx>=0 &&
                ny>=0 &&
                nx<4 &&
                ny<4 &&
                grid[nx][ny]===0
            ){
                queue.push([[nx,ny],[...path,[nx,ny]]]);
            }
        }
    }
}



// ===================
// CO3 CSP Localization
// ===================

function runCO3(){

    let possible=[];

    for(let x=0;x<4;x++){

        for(let y=0;y<4;y++){

            let wallNorth=(x===0);
            let wallWest=(y===0);

            if(wallNorth && wallWest){
                possible.push([x,y]);
            }
        }
    }

    document.getElementById("co3").innerHTML =
    "Possible Location: " + JSON.stringify(possible);
}