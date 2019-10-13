const btns= document.getElementsByName("play");


for (let i=0; i<btns.length; i++) {
    btns[i].addEventListener("click", function(){poster(btns[i].value)});
}


function poster(val){
    
    $.ajax({
        url: 'http://127.0.0.1:5000/rpta',
        type: 'post',
        data: val,
        contentType: false,
        datatype: raw,
        success: function (response) {
            alert('nope');
            if (response != 0) {
                console.log("Here");
            } else {
            }

        },

    });

}
    

