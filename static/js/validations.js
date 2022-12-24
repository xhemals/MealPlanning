function disableRest() {
    if (document.getElementById("id_who_is_eating_1").disabled == true) {
        document.getElementById("id_who_is_eating_1").disabled = false;
        document.getElementById("id_who_is_eating_2").disabled = false;
        document.getElementById("id_who_is_eating_3").disabled = false;
        document.getElementById("id_who_is_eating_4").disabled = false;
    }
    else {
        document.getElementById("id_who_is_eating_1").disabled = true;
        document.getElementById("id_who_is_eating_2").disabled = true;
        document.getElementById("id_who_is_eating_3").disabled = true;
        document.getElementById("id_who_is_eating_4").disabled = true;
    }
}
$(document).ready(function () {
    $("form").submit(function () {
        if ($('input:checkbox').filter(':checked').length < 1) {
            alert("Please select at least 1 person");
            return false;
        }
    });
});

function disableOnStart() {
    document.getElementById("id_who_is_eating_1").disabled = true;
    document.getElementById("id_who_is_eating_2").disabled = true;
    document.getElementById("id_who_is_eating_3").disabled = true;
    document.getElementById("id_who_is_eating_4").disabled = true;
}
