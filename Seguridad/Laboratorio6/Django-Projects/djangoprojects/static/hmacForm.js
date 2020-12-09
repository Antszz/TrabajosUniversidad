if ($('#hash').val() != 5)
    {
        document.getElementById("data-hmac").style.display = "none";
    };

$('#hash').change(function() {

    if ($('#hash').val() == 5)
    {
        document.getElementById("data-hmac").style.display = "block";
    }

    else
    {
        document.getElementById("data-hmac").style.display = "none";
    };

});