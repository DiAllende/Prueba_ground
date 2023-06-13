$(document).ready(function () {
  $("#register").submit(function (event) {
    event.preventDefault(); // Evita que la página se recargue al hacer clic en el botón de envío.

    // Obtén los valores de los campos de entrada.
    var nombre = $("#nombre").val();
    var numero = $("#numero").val();
    var email = $("#correo").val();
    var sexo = $("#sexo").val();

    // Muestra los valores en la vista de confirmación.
    $("#nombreConfirmacion").text(nombre);
    $("#numeroConfirmacion").text('+' + numero);
    $("#emailConfirmacion").text(email);
    $("#sexoConfirmacion").text(sexo);

    // Oculta el formulario y muestra la vista de confirmación.
    $("#register").hide();
    $("#vistaConfirmacion").show();
  });

  $("#botonAceptar").click(function () {
    $("#vistaConfirmacion").hide();
    $("#vistaMensaje").show();
  });

  $("#botonSiguiente").click(function () {
    $("#vistaMensaje").show();
    window.location.href = 'index.html';
  });

  $("#botonVolver").click(function () {
    $("#vistaConfirmacion").hide();
    $("#register").show();
  });
});