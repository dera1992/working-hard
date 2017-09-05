$(function() {

  $('#search').keyup(function() {

    $.ajax({
      type: 'POST',
      url : '/news/search/',
      data: {
           'search_text' : $('#search').val(),
           'csrfmiddlewaretoken' : $("input [name=csrfmiddlewaretoken]").val()
      },
      success: searchSuccess,
      dataType: 'html'
      });
    });
  });

function searchSuccess(data, textStatus,jqXHR)
{
  $('#search-results') . html(data);
}

// $( document ).ready( function() {
// $( '#search' ).click( function() {
// q = $( '#q' ).val();
// $( '#results' ).html( '&nbsp;' ).load( "{% url 'news:search' %}?q=" + q );
// });
// });
