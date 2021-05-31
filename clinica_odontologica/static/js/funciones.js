$(document).ready(function () {
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd',
        i18n: {
            months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
            ],
            monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct',
                'Nov', 'Dic'
            ],
            weekdays: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes',
                'Sábado'
            ],
            weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
            weekdaysAbbrev: ['D', 'L', 'M', 'M', 'J', 'V', 'S']
        }
    });
    $('select').formSelect();

    $('.timepicker').timepicker({
        twelveHour: false,
    });
    $(document).ready(function () {
        $('.tabs').tabs();
    });

    $('.modal').modal();
    $(".collapsible").collapsible();

});

$(document).ready(function () {
    $('#frmPaciente_buscar').change(function (e) {
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function (json) {
                for (var item in json) {
                    document.getElementById('nombres').value = json[item].nombres;
                    document.getElementById('apellidos').value = json[item].apellidos;
                    document.getElementById('telefono').value = json[item].telefono;
                }
            }
        });
    });

    $('#frmCita').change(function (e) {
        e.preventDefault();
        $.ajax({
            url: '/base/validarCita/',
            type: $(this).attr('method'),
            data: $(this).serialize(),
            success: function (json) {
                M.toast({ html: json })
            }
        });
    });
});

$(document).ready(function () {
    $('#example').DataTable({
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    });
});

$(document).ready(function () {
    $('.card-alert > button').on('click', function () {
        $(this).closest('div.card-alert').fadeOut('slow');
    })
})