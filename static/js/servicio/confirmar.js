
$('#reservar').change(function(){
		if ($(this).is(':checked')) {
			$('#fecha_re').removeAttr('readonly');
		}
	});

	$('#ahora').change(function(){
		if ($(this).is(':checked')) {
			$('#fecha_re').attr('readonly','readonly');
		}
	});
	