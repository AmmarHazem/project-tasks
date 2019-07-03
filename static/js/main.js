$(document).ready(function() {

    $('.select2-multiple').select2();

    $( ".date-selector" ).datepicker({
        dateFormat: "yy-mm-dd",
    });

    $('table .details').on('click', function(){

        let table = $(this).parents('table');
        let detailsRow = table.find('.details-row');
        if(detailsRow.hasClass('d-none')){
            detailsRow.removeClass('d-none')
        }
        else{
            detailsRow.addClass('d-none')
        }
    });
});
