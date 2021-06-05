const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
setTimeout(function () {

    $('.action_result').fadeOut('slow');
},10000);
