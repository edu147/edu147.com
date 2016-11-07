    // Binary Calculator

function changeBit(me) {
    bitVal = me.value;

    if (me.checked) {
        bit = document.getElementById("bit-" + bitVal).innerHTML=1;
    }
    else {
        bit = document.getElementById("bit-" + bitVal).innerHTML=0;
    }
}

function clearCb() {
    $('input[type="checkbox"]:checked').prop('checked',false);
    bits = document.getElementsByClassName("single-bit");
    for(var i=0; i<bits.length;i++) {
        bits[i].innerHTML=0;
    }
}

$(document).ready(function() {

    $('form[name="bit-counter"]').submit(function(event) {
        var bits = [];
        var decResult = 0;
        event.preventDefault();
        console.log("form submitted");
        $("input:checkbox[name='cb[]']:checked").each(function () {
            bits.push(parseInt($(this).val())); //return this.value;
        });
        for (i=0; i<bits.length; i++) {
            decResult += Math.pow(2, bits[i]);
        }
        console.log(bits + "\n" + decResult);

    });

});
