$(document).ready(function () {

    $("#formulario").submit(function (e) {

        var nombre = $("#nomUser").val();
        var ape = $("#apeUser").val();
        var mail = $("#email")
        var pass1 = $("#password1").val();
        var pass2 = $("#password2").val();

        let mensajeMostrar = "";
        let entrar = true;

        if (pass1 != pass2) {
            mensajeMostrar += "Las contraseñas no coinciden<br>";
            entrar = false;
        }
        if (entrar) {
            $("#mensajeReg").html("Registro exitoso");
        }
        else {
            $("#mensajeReg").html(mensajeMostrar);
            e.preventDefault();
        }
    });
})