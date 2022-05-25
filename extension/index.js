const goEl = document.getElementById("go-btn");
var inputEl = document.getElementById("input-el");
let num = -1;
let linkarr = [
  "https://ch01-livecdn.spotvnow.co.kr/ch01/ch01.smil/chunklist.m3u8",
  "https://ch02-livecdn.spotvnow.co.kr/ch02/ch02.smil/chunklist.m3u8",
  "https://ch03-livecdn.spotvnow.co.kr/ch03/ch03.smil/chunklist.m3u8",
  "https://ch04-livecdn.spotvnow.co.kr/ch04/ch04.smil/chunklist.m3u8",
  "https://ch05-livecdn.spotvnow.co.kr/ch05/ch05.smil/chunklist.m3u8",
  "https://ch06-livecdn.spotvnow.co.kr/ch06/ch06.smil/chunklist.m3u8",
  "https://ch07-livecdn.spotvnow.co.kr/ch07/ch07.smil/chunklist.m3u8",
  "https://ch08-livecdn.spotvnow.co.kr/ch08/ch08.smil/chunklist.m3u8",
  "https://ch09-livecdn.spotvnow.co.kr/ch09/ch09.smil/chunklist.m3u8",
];

goEl.addEventListener("click", function () {
  switch (inputEl.value) {
    case "":
      ShowWarning();
      break;
    case "1":
      num = 0;
      break;
    case "2":
      num = 1;
      break;
    case "3":
      num = 2;
      break;
    case "4":
      num = 3;
      break;
    case "5":
      num = 4;
      break;
    case "6":
      num = 5;
      break;
    case "7":
      num = 6;
      break;
    case "8":
      num = 7;
      break;
    case "9":
      num = 8;
      break;
  }
  inputEl.value = "";
  if (num != -1) {
    GotoLink(num);
  }
});

function GotoLink(n) {
  num = -1;
  var link = linkarr[n];
  window.open(
    link,
    "_blank",
    "toolbar=yes,scrollbars=yes,resizable=yes,fullscreen=yes"
  );
}

function ShowWarning() {
  alert("입력한 값이 없습니다. 1~9사이의 수를 입력하세요.");
}
