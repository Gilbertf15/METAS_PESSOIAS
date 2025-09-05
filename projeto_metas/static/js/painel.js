///function alterar() {
//  const navegacao = document.getElementById("nav-lateral");
//const estilo = window.getComputedStyle(navegacao).display;
//document.getElementById("abrir-nav").addEventListener("click", function () {
// if (estilo === "flex") {
//  document.getElementById("nav-lateral").style.display = "none";
//} else {
// document.getElementById("nav-lateral").style.display = "flex";
//}
//});
//}//
function inserirestilo() {
  const estilo = document.getElementById("nav-lateral");
  const verificar = window.getComputedStyle(estilo).display;
  estilo.classList.toggle("abrir-navegacao");
}
