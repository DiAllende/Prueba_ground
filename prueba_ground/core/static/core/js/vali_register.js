function validateForm() {
    const form = document.querySelector('.needs-validation');
    if (form.checkValidity() === false) {
    event.preventDefault();
    event.stopPropagation();
    } else {
    window.location.href = "index.html";
    }
    form.classList.add('was-validated');
        var passwordInput = document.getElementById("validationCustom06");
        var passwordValidation = document.getElementById("passwordValidation");
    
        // Verificar la longitud mínima de la contraseña
        if (passwordInput.value.length < 6) {
            passwordValidation.textContent = "La contraseña debe tener al menos 6 caracteres.";
            passwordInput.classList.add("is-invalid");
            passwordInput.classList.remove("is-valid");
        } else {
            passwordValidation.textContent = "";
            passwordInput.classList.remove("is-invalid");
            passwordInput.classList.add("is-valid");
        }
    }


function validateRut(rut) {
    rut = rut.replace(/[^0-9kK]+/g, '').toUpperCase();
    if (rut.length < 2) return false;
    let digits = [...rut];
    const verifier = digits.pop();
    let sum = 0;
    let multiplier = 2;
    for (let i = digits.length - 1; i >= 0; i--) {
        sum += digits[i] * multiplier;
        multiplier = (multiplier + 1) % 8 || 2;
    }
    const expectedVerifier = '0' + (11 - sum % 11);
    return verifier === expectedVerifier.slice(-1);
}

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validateAddress(address) {
    const addressRegex = /^.*\d{3,}.*$/;
    return addressRegex.test(address);
}

function validatePostalCode(postalCode) {
    const postalCodeRegex = /^[0-9]{7}$/;
    return postalCodeRegex.test(postalCode);
}

const rutInput = document.getElementById('validationCustom02');
rutInput.addEventListener('input', () => {
    const isValid = validateRut(rutInput.value);
    rutInput.setCustomValidity(isValid ? '' : 'Rut inválido');
});

const emailInput = document.getElementById('validationCustomUsername');
emailInput.addEventListener('input', () => {
    const isValid = validateEmail(emailInput.value);
    emailInput.setCustomValidity(isValid ? '' : 'Correo inválido');
});

const addressInput = document.getElementById('validationCustom03');
addressInput.addEventListener('input', () => {
    const isValid = validateAddress(addressInput.value);
    addressInput.setCustomValidity(isValid ? '' : 'Dirección inválida. Asegúrate de ingresar una dirección válida en Chile.');
});

const postalCodeInput = document.getElementById('validationCustom05');
postalCodeInput.addEventListener('input', () => {
    const isValid = validatePostalCode(postalCodeInput.value);
    postalCodeInput.setCustomValidity(isValid ? '' : 'Código postal inválido en Chile. El formato debe ser de 7 dígitos.');
});


