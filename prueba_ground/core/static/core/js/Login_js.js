const form = document.querySelector("form");
eField = form.querySelector(".email"),
eInput = eField.querySelector("input"),
pField = form.querySelector(".password"),
pInput = pField.querySelector("input");
form.onsubmit = (e)=>{
  e.preventDefault(); //impedir el envío de formularios
  //Si el correo electrónico y la contraseña están en blanco, agregue la clase Shake y llame a la función especificada
  (eInput.value == "") ? eField.classList.add("shake", "error") : checkEmail();
  (pInput.value == "") ? pField.classList.add("shake", "error") : checkPass();
  setTimeout(()=>{ //Eliminar la clase de shake después de 500ms
    eField.classList.remove("shake");
    pField.classList.remove("shake");
  }, 500);
  eInput.onkeyup = ()=>{checkEmail();} //llamar a la función checkEmail en email input keyup
  pInput.onkeyup = ()=>{checkPass();} //llamar a la función checkPassword en pass input keyup
  function checkEmail(){ //checkEmail
    let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; //pattern para validar email
    if(!eInput.value.match(pattern)){ //si el pattern no coincide, agrega el error y quita la clase valid
      eField.classList.add("error");
      eField.classList.remove("valid");
      let errorTxt = eField.querySelector(".error-txt");
      //si email no esta vacio, muestra el mensaje: Correo ingresado no valido, si no que muestre el mensaje: El correo no puede estar vacio
      (eInput.value != "") ? errorTxt.innerText = "Correo ingresado no valido" : errorTxt.innerText = "El correo no puede estar vacio";
    }else{ //si pattern coincide, quita el error y agrega la clase valid
      eField.classList.remove("error");
      eField.classList.add("valid");
    }
  }
  function checkPass(){ //checkPass function
    if(pInput.value == ""){ //si pass esta vacio, agrega el error y remueve la clase valid
      pField.classList.add("error");
      pField.classList.remove("valid");
    }else{ //si pass esta vacio, remueve el error y agregac la clase valid
      pField.classList.remove("error");
      pField.classList.add("valid");
    }
  }
}
