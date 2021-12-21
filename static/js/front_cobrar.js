$(document).ready(function() {
    $('#fecha').val(currentDate());
    $('#intereses').val(0);
    $('#extras').val(0);
    $('#descuento').val(0);
    calcularIntereses();
    calcularTotalRecibo();
});

function calcularTotalRecibo() {
    let totalRecibo = 0;
    totalRecibo = (parseFloat($('#valor_alquiler').val()) + parseFloat($('#intereses').val()) + parseFloat($('#extras').val())) - parseFloat($('#descuento').val());
    $('#total_recibo').val(totalRecibo);
}

function calcularIntereses() {
    let intereses = 0;
    const date1 = new Date($('#fecha_vencimiento').val());
    const date2 = new Date($('#fecha').val());
    const diffTime = date2 - date1;
    let diffDays = 0;
    if (diffTime > 0) {
        diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    }
    intereses = ((parseFloat($('#interes_diario').val()) * diffDays) / 100) * parseFloat($('#valor_alquiler').val());
    $('#intereses').val(intereses);
    calcularTotalRecibo();
}

$( "#fecha" ).change(function() {
  calcularIntereses();
});

$( ".valores" ).change(function() {
  calcularTotalRecibo();
});

function currentDate() {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = yyyy + '-' + mm + '-' + dd;
    return today;
}