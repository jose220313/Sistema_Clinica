$('#pacienteFormBtn').on('click', function () {
    let peso = document.getElementById('peso');
    let pulso = document.getElementById('pulso');
    let temperatura = document.getElementById('temperatura');
    let presion_arterial = document.getElementById('presion_arterial');
    let errorPeso = document.getElementById('errorPeso');
    let errorPulso = document.getElementById('errorPulso');
    let errorTemperatura = document.getElementById('errorTemperatura');
    let errorPresion = document.getElementById('errorPresion');
    let telefono = document.getElementById('telefono');
    let errorTelefono = document.getElementById('errorTelefono');
    let telefono_medico = document.getElementById('telefono_medico');
    let errorTelefono_medico = document.getElementById('errorTelefono_medico');

    $(document).ready(telefono);

    function validarTelefono(param) {
        let patron = /^\d{4}-\d{4}/;
        if (!patron.test(param)) {
            return false;
        } else {
            return true;
        }
    }
    // VALIDACIÓN DE TELEFONO
    if (telefono.value == "") {
        errorTelefono.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Telefono Vacio. Ingrese la información necesaria</div>';
    } else if (validarTelefono(telefono.value) == false) {
        errorTelefono.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Telefono Invalido</div>';
    } else if (validarTelefono(telefono.value) == true) {
        errorTelefono.innerHTML = '<div>Telefono</div>';
    }

    // VALIDACIÓN DE TELEFONO MEDICO
    if (validarTelefono(telefono_medico.value) == false) {
        errorTelefono_medico.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Telefono Invalido</div>';
    } else if (validarTelefono(telefono_medico.value) == true) {
        errorTelefono_medico.innerHTML = '<div>Telefono</div>';
    }
    // VALIDACIÓN DE PESO
    if (peso.value == "") {
        errorPeso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Peso Vacio. Ingrese la información necesaria</div>';
    } else if (peso.value < 0) {
        errorPeso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Peso no puede ser negativo</div>';
    } else if (peso.value < 5) {
        errorPeso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Peso no esta en el rango real de una persona (rango: 5 - 900 lb)</div>';
    } else if (peso.value > 900) {
        errorPeso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Peso no esta en el rango real de una persona (rango: 5 - 900 lb)</div>';
    } else {
        errorPeso.innerHTML = '<div>Peso (lb)</div>';
    }


    // VALIDACIÓN DE PULSO  
    if (pulso.value == "") {
        errorPulso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Pulso Vacio. Ingrese la información necesaria</div>';
    } else if (pulso.value < 0) {
        errorPulso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo pulso no puede ser negativo</div>';
    } else if (pulso.value < 70) {
        errorPulso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Pulso no real de una persona (rango: 70 - 200 Latidos/Min.)</div>';
    } else if (pulso.value > 200) {
        errorPulso.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Pulso no real de una persona (rango: 70 - 200 Latidos/Min.)</div>';
    } else {
        errorPulso.innerHTML = '<div>Pulso (Latidos/Min.)</div>';
    }


    // VALIDACIÓN DE TEMPERATURA
    if (temperatura.value == "") {
        errorTemperatura.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Temperatura Vacio. Ingrese la información necesaria</div>';
    } else if (temperatura.value < 0) {
        errorTemperatura.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo temperatura no puede ser negativo</div>';
    } else if (temperatura.value < 34) {
        errorTemperatura.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Temperatura no real de una persona (rango: 34 - 42.5 (Celsius))</div>';
    } else if (temperatura.value > 42.5) {
        errorTemperatura.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Temperatura no real de una persona (rango: 34 - 42.5 (Celsius))</div>';
    } else {
        errorTemperatura.innerHTML = '<div>Temperatura (Celsius)</div>';
    }


    // VALIDACIÓN DE PRESION
    if (presion_arterial.value == "") {
        errorPresion.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Presión Arterial Vacio. Ingrese la información necesaria</div>';
    } else if (presion_arterial.value < 0) {
        errorPresion.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Presión Arterial no puede ser negativo</div>';
    } else if (presion_arterial.value < 80) {
        errorPresion.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Presión Arterial no real de una persona (rango: 80 - 150 (mmHg))</div>';
    } else if (presion_arterial.value > 150) {
        errorPresion.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Presión Arterial no real de una persona (rango: 80 - 150 (mmHg))</div>';
    } else {
        errorPresion.innerHTML = '<div>Presión Arterial (mmHg)</div>';
    }
});

// FUNCION DE GUION AUTOMATICO TELEFONOS
$(document).ready(telefono);
function telefono() {
    var temp = true;
    $(document).on('keyup', '[id=telefono]', function (e) {
        if ($(this).val().length == 4 && temp) {
            $(this).val($(this).val() + "-");
            temp = false;
        }
    });
}

$(document).ready(telefono_medico);
function telefono_medico() {
    var temp = true;
    $(document).on('keyup', '[id=telefono_medico]', function (e) {
        if ($(this).val().length == 4 && temp) {
            $(this).val($(this).val() + "-");
            temp = false;
        }
    });
}

// TELEFONO CITAS
$('#citaFormBtn').on('click', function () {
    let telefono = document.getElementById('telefono');
    let errorTelefono = document.getElementById('errorTelefono');

    function validarTelefono(param) {
        let patron = /^\d{4}-\d{4}/;
        if (!patron.test(param)) {
            return false;
        } else {
            return true;
        }
    }
    // VALIDACIÓN DE TELEFONO
    if (telefono.value == "") {
        errorTelefono.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Campo Telefono Vacio. Ingrese la información necesaria</div>';
    } else if (validarTelefono(telefono.value) == false) {
        errorTelefono.innerHTML = '<div style="font-size: 12px; color:rgb(236, 98, 98)">Telefono Invalido</div>';
    } else if (validarTelefono(telefono.value) == true) {
        errorTelefono.innerHTML = '<div>Telefono</div>';
    }
});