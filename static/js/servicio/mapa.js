$('#cargando').slideDown();	



var rendererOptions = {
draggable: true
};
var centro = new google.maps.LatLng(10.072523, -69.320846);
var directionsDisplay = new google.maps.DirectionsRenderer(rendererOptions);;
var directionsService = new google.maps.DirectionsService();
var map;

function initialize() {

  var mapOptions = {
		    zoom: 16,
      	center: centro
  		};

  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  directionsDisplay.setMap(map);

function todo() {
    var origen = $('#origen').val();
    var destino = $('#destino').val();
      if (origen == "" || destino == "") {
        alert("Llene todos los campos");
      } else {
        $('#cargando').show();
        $('#btn-confirmar').hide();
          document.getElementById('total').innerHTML = '';
          calcRoute(origen, destino);
      }

}
  $('#calcular').click(function(){
    todo();
  });

  	google.maps.event.addListener(directionsDisplay, 'directions_changed', function() {
    computeTotalDistance(directionsDisplay.getDirections());
	});
}

function calcRoute(origen,destino) {

  var request = {
		origin: origen + 'Barquisimeto',
        destination: destino + 'Barquisimeto',
        travelMode: google.maps.TravelMode.DRIVING,
        optimizeWaypoints: false,
        region: 'VE'
  };
  directionsService.route(request, function(response, status) {
      if (status == google.maps.DirectionsStatus.OK) {
        //Si funciona
        directionsDisplay.setDirections(response);
        $('#cargando').hide();
        $('#btn-confirmar').show();
        bandera = true
      
      } else {      
        bandera = false
        $('#cargando').hide();
        alert('Error en la consulta, por favor intente de nuevo');
      }
      });
}

function computeTotalDistance(result) {
  var total = 0;
  var myroute = result.routes[0];
  for (var i = 0; i < myroute.legs.length; i++) {
    total += myroute.legs[i].distance.value;
  }
  total = total / 1000.0;
  document.getElementById('total').innerHTML = total + ' km';

  $("input*[name='origen']").val(myroute.legs[0].start_address);
  $("input*[name='destino']").val(myroute.legs[0].end_address); 
  $('.distancia-form').val(total);

}

  google.maps.event.addDomListener(window, 'load', initialize);
  
 