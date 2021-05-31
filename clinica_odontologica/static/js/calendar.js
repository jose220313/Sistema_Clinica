$(document).ready(function () {
    var calendar = $('#calendar').fullCalendar({
        defaultTimedEventDuration: '01:00:00',
        forceEventDuration: true,
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        events: [
            {% for cita in citas %}
                {
                    title: "ID de CITA: "+"{{cita.id_cita}}"+" MOTIVO: "+"{{cita.motivo_consulta}}" + 
                    {%if cita.id_paciente%}
                    " ID del paciente: "+ "{{cita.id_paciente}} "+" NOMBRES: "+"{{cita.id_paciente.nombres}}"+" "+"{{cita.id_paciente.apellidos}}",
                    {% else %}
                    " NOMBRES: "+"{{cita.nombres}}"+" "+"{{cita.apellidos}}",
                    {%endif%}
                    start: "{{cita.fecha|date:'Y-m-d'}}"+" "+"{{cita.hora|date:'H:i:s'}}",
                    allDay:false,
                    id:"{{cita.id_cita}}"
                },
            {% endfor %}
        ],
        selectable: true,
        selectHelper: true,
        editable: true,
        eventLimit: true,

    });
});
