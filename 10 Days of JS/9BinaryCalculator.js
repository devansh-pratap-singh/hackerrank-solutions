// HTML
// <!DOCTYPE html >
// <html>
//     <head>
//         <meta charset="utf-8">
//         <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
//         <title>Binary Calculator</title>
//     </head>
//     <body>
//         <div id ="res" class="resultClass"> </div>
//         <div id="btns" class="buttonContainer">
//             <button id="btn0" class="buttonClass"> 0 </button>
//             <button id="btn1" class="buttonClass"> 1 </button>
//             <button id="btnClr" class="buttonClass"> C </button>
//             <button id="btnEql" class="buttonClass"> = </button>
//             <button id="btnSum" class="buttonClass"> + </button>
//             <button id="btnSub" class="buttonClass"> - </button>
//             <button id="btnMul" class="buttonClass"> * </button>
//             <button id="btnDiv" class="buttonClass"> / </button>
//         </div>
//         <script src="js/binaryCalculator.js" type="text/javascript"></script>
//     </body>
// </html>

// CSS
// body {
//     width: 33%;
// }

// #res {
//     background-color: lightgray;
//     border: solid;
//     height: 48px;
//     font-size: 20px;
// }

// #btn0, #btn1 {
//     background-color: lightgreen;
//     color: brown;
// }

// #btnClr, #btnEql {
//     background-color: darkgreen;
//     color: white;
// }

// #btnSum, #btnSub, #btnMul, #btnDiv {
//     background-color: black;
//     color: red;
// }

// .buttonClass {
//     width: 25%;
//     height: 36px;
//     font-size: 18px;
//     margin: 0px;
//     float: left;
// }

// JavaScript
document.getElementById("btn0").addEventListener("click", function () {
	document.getElementById("res").insertAdjacentHTML("beforeend", "0");
});

document.getElementById("btn1").addEventListener("click", function () {
	document.getElementById("res").insertAdjacentHTML("beforeend", "1");
});

function operatorAction(eve) {
	var btn = eve.target;
	document.getElementById("res").insertAdjacentHTML("beforeend", btn.innerHTML);
}

document.getElementById("btnSum").onclick = operatorAction;
document.getElementById("btnMul").onclick = operatorAction;
document.getElementById("btnDiv").onclick = operatorAction;
document.getElementById("btnSub").onclick = operatorAction;

document.getElementById("btnClr").onclick = function () {
	document.getElementById("res").innerHTML = "";
};
