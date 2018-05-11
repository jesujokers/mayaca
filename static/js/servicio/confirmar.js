
$('#reservar').change(function(){
		if ($(this).is(':checked')) {
			$('#fecha_re').removeAttr('readonly');
			$('#fecha_re').attr('required','required');
		}
	});

	$('#ahora').change(function(){
		if ($(this).is(':checked')) {
			$('#fecha_re').attr('readonly','readonly');
			$('#fecha_re').removeAttr('required');
		}
	});
	