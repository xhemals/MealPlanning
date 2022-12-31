$(document).ready(function () {
    failedForm = false;
    fine = false;
    if ($("#id_who_is_eating_0").prop('checked')) {
        disableOnStart();
    };

    $("#id_who_is_eating_0").on("click", function () {
        disableRest();
    });

    $("#id_other").hide();
    let checked = $("#id_who_is_eating_5").prop('checked')
    if (checked) {
        $("#id_other").show();
    };

    $("#id_who_is_eating_5").on("click", function () {
        $("#id_other").toggle();
    })

    // $("#id_who_is_eating_5").on("click", function () {
    //     let checked = $("#id_who_is_eating_5").prop('checked')
    //     if (!checked) {
    //         console.log("hide");
    //         $("#div_id_other").hide();
    //     }
    //     else {
    //         console.log("show");
    //         $("#div_id_other").show();
    //     }
    //     if (!executed) {
    //         const textBoxContainer = document.getElementById("div_id_other");
    //         const textBox = document.createElement("input");
    //         textBox.type = "text";
    //         textBox.name = "other";
    //         textBox.className = "textinput textInput form-control";
    //         textBox.id = "id_other_persons_0";
    //         textBox.style = "display: block;";
    //         textBoxContainer.appendChild(textBox);
    //         document.getElementById('id_other_persons_0').focus();
    //         executed = true;
    //     }
    // })
    $("#id_other").keydown(function (event) {
        var text = $(this).val();
        if (event.key === ",") {
            event.preventDefault();
            $(this).val(text + ", ");
        }
    });

    $('#meal_form_id').keypress(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    });
    // var boxNum = 0;
    // $('#div_id_other').keypress(function (event) {
    //     const textBoxContainer = document.getElementById("div_id_other");
    //     if (event.keyCode == 13) {
    //         boxNum++;
    //         array = new Array(boxNum);
    //         const textBox = document.createElement("input");
    //         textBox.type = "text";
    //         textBox.name = "other";
    //         textBox.className = "textinput textInput form-control";
    //         textBox.id = "id_other_" + boxNum;
    //         textBox.style = "display: block;";
    //         textBoxContainer.appendChild(textBox);
    //         document.getElementById('id_other_' + boxNum).focus();
    //     }
    // })
    // document.querySelector('#submit-id-submit').addEventListener('click', function () {
    //     var values = "";
    //     for (let i = 1; i < array.length; i++) {
    //         let textBox = document.querySelector('#id_other_' + i);
    //         let textValue = textBox.value;
    //         let mainBox = document.querySelector("#id_other");
    //         if (values != "") {
    //             console.log("full")
    //             var combined = values.concat(", ", textValue);
    //             values = combined;
    //         }
    //         else {
    //             console.log("empty")
    //             var values = mainBox.value;
    //             var combined = values.concat(", ", textValue);
    //             values = combined;
    //         }
    //         mainBox.value = values;
    //         console.log(values);
    //     }
    // });

    $('input[type="text"]').keydown(function (e) {
        if (e.key === ' ' && $(this).val().endsWith(' ')) {
            e.preventDefault();
            let value = $(this).val();
            $(this).val(value.substring(0, value.length));
        }
        if (e.key === ',' && $(this).val().endsWith(', , ')) {
            let value = $(this).val();
            $(this).val(value.substring(0, value.length - 2));
        }
        if (e.key === ',' && $(this).val().endsWith(',')) {
            let value = $(this).val();
            $(this).val(value.substring(0, value.length - 1));
        }
        if (e.key === ' ' && $(this).val().length === 0) {
            e.preventDefault();
        }
        if (e.key === ',' && $(this).val().startsWith(', ')) {
            let value = $(this).val();
            $(this).val(value.substring(2));
        }
    });

    $('input[type="text"]').blur(function () {
        let value = $(this).val();
        if (value.endsWith(' ') || value.endsWith(',') || value.endsWith(', ')) {
            $(this).val(value.substring(0, value.length - 1));
        }
        if (value.endsWith(', ')) {
            $(this).val(value.substring(0, value.length - 2));
        }
    });

    $("#meal_form_id").submit(function () {
        if (document.getElementById("id_other").value == "") {
            document.getElementById("id_who_is_eating_5").checked = false;
        }
    });


    //Loading
    var buttonSubmit = document.getElementById("submit-id-submit");
    var form = document.getElementById("start_form_id");
    var formMeal = document.getElementById("meal_form_id");
    var formDelete = document.getElementById("delete_form_id");
    var buttonHome = document.getElementById("home");
    if (form) {
        form.addEventListener("submit", function () {
            if (this.checkValidity()) {
                buttonSubmit.value = "Loading";
                var dots = "";
                var interval = setInterval(function () {
                    dots = (dots.length === 3) ? "" : dots + ".";
                    buttonSubmit.value = "Loading" + dots;
                }, 100);
            }
        });
    };

    if (formMeal) {
        formMeal.addEventListener("submit", function () {
            if ($('#id_who_is_eating_0:checked, #id_who_is_eating_1:checked, #id_who_is_eating_2:checked, #id_who_is_eating_3:checked, #id_who_is_eating_4:checked').length == 0) {
                alert("Please select at least 1 person from the household");
                event.preventDefault();
                document.getElementById('id_who_is_eating_5').prop('checked', true);
            }
            else {
                buttonSubmit.value = "Loading";
                var dots = "";
                var interval = setInterval(function () {
                    dots = (dots.length === 3) ? "" : dots + ".";
                    buttonSubmit.value = "Loading" + dots;
                }, 100);
            }
        });
    };

    if (formDelete) {
        formDelete.addEventListener("submit", function () {
            if (this.checkValidity()) {
                buttonSubmit.value = "Loading";
                var dots = "";
                var interval = setInterval(function () {
                    dots = (dots.length === 3) ? "" : dots + ".";
                    buttonSubmit.value = "Loading" + dots;
                }, 100);
            };
        });
    };

    buttonHome.addEventListener("click", function () {
        var dots = "";
        function animateText() {
            dots = (dots.length === 3) ? "" : dots + ".";
            buttonHome.innerHTML = "<b>Loading" + dots + "</b>";
        }
        var interval = setInterval(animateText, 100);
    })
    var editBtn = document.querySelectorAll("[id^='edit_btn_']");
    for (let element of editBtn) {
        element.addEventListener("click", function () {
            document.getElementById(element.id).innerHTML = "Loading"
            var count = 0;
            setInterval(function () {
                count++;
                var dots = new Array(count % 5).join('.');
                document.getElementById(element.id).innerHTML = "Loading" + dots;
            }, 100);
        })
    };

    var deleteBtn = document.querySelectorAll("[id^='delete_btn_']");
    for (element of deleteBtn) {
        element.addEventListener("click", function () {
            document.getElementById(element.id).innerHTML = "Loading"
            var count = 0;
            setInterval(function () {
                count++;
                var dots = new Array(count % 5).join('.');
                document.getElementById(element.id).innerHTML = "Loading" + dots;
            }, 100);
        })
    }
});

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
};

function disableOnStart() {
    document.getElementById("id_who_is_eating_1").disabled = true;
    document.getElementById("id_who_is_eating_2").disabled = true;
    document.getElementById("id_who_is_eating_3").disabled = true;
    document.getElementById("id_who_is_eating_4").disabled = true;
};