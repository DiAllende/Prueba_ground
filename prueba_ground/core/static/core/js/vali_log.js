function valiLog(){
    var usuario = document.getElementById('Uname_log');
    var pass = document.getElementById('password_log');
    var error_uname = document.getElementById('error_uname');
    var error_pass = document.getElementById('error_pass');
    error_uname.style.color = "red";
    error_pass.style.color = "red";
    
    
    if(usuario.value == "" && pass.value == "" || usuario.value == " " && pass.value == " "){
        error_uname.innerHTML = ("(El usuario debe ser completado)");
        error_pass.innerHTML = ("(la contraseña debe ser completada)");
        return false;
    }
    else if(usuario.value == "" && pass.value == " " || usuario.value == " " && pass.value == ""){
        error_uname.innerHTML = ("(El usuario debe ser completado)");
        error_pass.innerHTML = ("(la contraseña debe ser completada)");
        return false;
    }
    else if(usuario.value == "" || usuario.value == " "){
        error_pass.innerHTML =("");
        error_uname.innerHTML = ("(El usuario debe ser completado)");
        return false;
    }
    else if(pass.value == "" || pass.value == " "){
        error_uname.innerHTML =("");
        error_pass.innerHTML = ("(la contraseña debe ser completada)");
        return false;
    } else if (pass.value.length < 8) {
        error_uname.innerHTML =("");
        error_pass.innerHTML = '(La contraseña debe tener al menos 8 caracteres)';
    }
    else{
        error_uname.innerHTML =("");
        error_pass.innerHTML =("");
        document.location.assign('home.html')
    }
    
}