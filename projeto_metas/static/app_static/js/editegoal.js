var barra = document.getElementById("id_current_value");

console.log(barra.value);

document
  .getElementById("id_current_value")
  .addEventListener("input", function () {
    const valor = this.value;
    document.getElementById("goal").textContent = valor + "0%";
    console.log(valor);
  });
