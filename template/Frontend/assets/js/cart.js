const url = 'http://127.0.0.1:8000/cart/get_cart_count/'
$.get(url, function(data){
$('#cartcounthead').text(data);
})
