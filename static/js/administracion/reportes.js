

$(document).ready(function () {

	$("#especifico").change(function () {
		if($("#especifico").is(':checked')) {
			$("#predefinida").removeAttr("disabled");
			$("#rango").removeAttr("disabled");
			$("#rango_fecha").removeAttr("disabled");
		} 


	}); 

	$("#general").change(function () {
		if($("#general").is(':checked')) {
			$("#predefinida").attr("disabled","");
			$("#rango").attr("disabled","");
			$("#rango_fecha").attr("disabled","");
		}
	}


})