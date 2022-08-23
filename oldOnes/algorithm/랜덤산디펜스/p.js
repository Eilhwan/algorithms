var data = require("./mountain.json");
var fs = require("fs");
var section = [
  "수도권",
  "강원권",
  "충남권",
  "충북권",
  "경북권",
  "경남권",
  "전남권",
];
var index = 1;
let num = 0;
for (var i = 0; i < section.length; i++) {
  num += data[section[i]].length;
}

var sectionTimes = new Array(section.length);
var mountainTimes = new Array(num);

sectionTimes.fill(0);
mountainTimes.fill(0);

for (var i = 0; i < 1000000; i++) {
  if (index % 3 !== 0) {
    console.log("...");
  } else {
    let randomNum = Math.floor(Math.random() * 100);
    var goSectionIndex = randomNum % section.length;
    var goSection = data[section[goSectionIndex]];
    let randomNum2 = Math.floor(Math.random() * 100);
    var realIndex = randomNum2 % data[section[goSectionIndex]].length;

    console.log(
      `우리가 가야 할 산은 ${section[goSectionIndex]} 지역의 ${goSection[realIndex]} 입니다.`
    );

    if (
      section[goSectionIndex] == "강원권" ||
      section[goSectionIndex] == "전남권" ||
      section[goSectionIndex] == "경남권"
    ) {
      console.log("준비 단단히 하세요...");
    }
    sectionTimes[goSectionIndex] += 1;
    var iiv = 0;
    for (var j = 0; j < goSectionIndex; j++) {
      iiv += data[section[goSectionIndex]].length;
    }
    mountainTimes[iiv + realIndex] += 1;
  }
  console.log(index);
  index++;
}

mainFunc;
