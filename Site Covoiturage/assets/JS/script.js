// Code JavaScript pour afficher la fenêtre modale
document.addEventListener("DOMContentLoaded", function () {
  var modal = document.getElementById("modal");
  var link = document.querySelector(".connexion-link");
  var closeBtn = document.getElementById("modal-close");

  link.addEventListener("click", function (e) {
    e.preventDefault();
    modal.style.display = "flex";
  });

  closeBtn.addEventListener("click", function () {
    modal.style.display = "none";
  });
});
document.getElementById("searchButton").addEventListener("click", function() {
  var input = document.getElementById("searchInput").value;
  // Ici, vous pourriez implémenter la logique de recherche en fonction de la valeur de 'input'
  alert("Vous avez recherché : " + input);
});
