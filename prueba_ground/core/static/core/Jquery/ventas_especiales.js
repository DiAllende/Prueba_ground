$(document).ready(function() {
  var container = $("#container");

  function ajustarItemsPorFila() {
    var windowWidth = $(window).width();
    var itemsPorFila = windowWidth >= 576 ? 3 : 2; 

    container.find(".col").removeClass("col-md-4 col-sm-6").addClass("col-md-" + (12 / itemsPorFila));
  }

  ajustarItemsPorFila();
  $(window).resize(ajustarItemsPorFila);

  $.get("https://fakestoreapi.com/products", function(data) {
    $.each(data, function(i, item) {
      var card = $("<div class='col-md-4 col-sm-6'>  "+
                    "<div class='card' style='width: 18rem;'>"+
                    "<img class='card-img-top' src='"+item.image+"' height='180' width='286px' alt='Card image cap'>"+
                    "<div class='card-body'>"+
                      "<h5 class='card-title'>"+item.title+"</h5>"+
                      "<p class='card-text'>"+item.price+"</p>"+
                      "<a href='carrito.html' class='btn btn-primary' id='details'>Comprar</a>"+
                    "</div>"+
                  "</div></div>"
                 );

        $("#ventas_es").append(card);
      });
    });
  });