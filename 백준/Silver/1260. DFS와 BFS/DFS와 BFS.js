const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
first = input[0].split(" ");
const n = Number(first[0]);
const m = Number(first[1]);
const v = Number(first[2]);

let visited = Array.from({ length: n }, () => 0);
let index = new Array();
let dfsanswer = [v];

for (let i = 0; i < n; i++) {
  index.push(new Array());
}

for (let i = 1; i < m + 1; i++) {
  tmp = input[i].split(" ");
  let a = Number(tmp[0]);
  let b = Number(tmp[1]);
  index[a - 1].push(b - 1);
  index[b - 1].push(a - 1);
}

for (let i = 0; i < n; i++) {
  index[i].sort((a, b) => a - b);
}

function dfs(v, visited) {
  willGo = new Array();
  visited[v] = 1;
  index[v].forEach((e) => {
    if (visited[e] == 0) {
      willGo.push(e);
      visited[e] = 1;
      dfsanswer.push(e + 1);
      dfs(e, visited);
    }
  });
}

function bfs(v, n) {
  let queue = [v];
  let visited = Array.from({ length: n }, () => 0);
  let ans = [v + 1];
  visited[v] = 1;
  while (queue.length > 0) {
    index[queue[0]].forEach((e) => {
      if (visited[e] == 0) {
        ans.push(e + 1);
        queue.push(e);
        visited[e] = 1;
      }
    });
    queue.shift();
  }
  return ans;
}

function print(arr) {
  console.log(arr.join(" "));
}

dfs(v - 1, visited);
print(dfsanswer);
print(bfs(v - 1, n));
