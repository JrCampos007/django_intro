function goBack() {                 // this is for the goBack button on the results page 
    window.history.back();
}

$(document).ready(function () {         
    $('#submit').click(function() {     
    checked = $("input[type=checkbox]:checked").length;

    if(!checked) {
        alert("You must check at least one checkbox.");
        return false;
    }

    });
});