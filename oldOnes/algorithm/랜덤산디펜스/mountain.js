var fs = require("fs");

var mountains = `
수도권
감악산
관악산
도봉산
마니산
명지산
백운산
북한산
소요산
용문산
운악산
유명산
천마산
축령산
화악산
강원권
가리산
가리왕산
계방산
공작산
대암산
덕항산
두타산
명성산
방태산
백덕산
백운산
삼악산
설악산
오대산
오봉산
용화산
점봉산
치악산
태백산
태화산
팔봉산
충남권
계룡산
대둔산
덕숭산
서대산
칠갑산
충북권
구병산
금수산
도락산
민주지산
소백산
속리산
월악산
천태산
희양산
경북권
가야산
금오산
경주 남산
내연산
대야산
비슬산
성인봉
운문산
응봉산
주왕산
주흘산
청량산
팔공산
황악산
황장산
경남권
가지산
금산
금정산
무학산
미륵산
신불산
연화산
재약산
지리산(智異山) [1]
통영 지리산(智異山) [2]
천성산
화왕산
황령산
황매산
황석산
전남권
지리산
두륜산
무등산
백운산
월출산
조계산
천관산
봉화산
팔영산
전북권
강천산
내장산
덕유산
마이산
모악산
방장산
백암산
변산
선운산
운장산
장안산
적상산
`;

let mtList = mountains.split("\n");
let index = 1;
let object = {};
let nameList = [];
for (var i = 2; i < mtList.length; i++) {
  if (mtList[i].indexOf("권") > -1) {
    object[mtList[index]] = mtList.slice(index + 1, i);
    nameList.push(mtList[index]);
    index = i;
  }
}
console.log(nameList);
var data = JSON.stringify(object);

// fs.writeFile("mountain.json", data, (err) => {});
