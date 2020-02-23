// var canvas = document.getElementById("myCanvas");
// var ctx = canvas.getContext("2d");
// var width = canvas.width, height = canvas.height;

console.log("in js")

window.color = '#3EAF3A';

 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;


function draw (xcoord, ycoord, color, div) {
    $.ajax({
            url: '/canvas/',
            type: 'post',
            data: {'xcoord': xcoord, 'ycoord' : ycoord, 'color' : color, csrfmiddlewaretoken: getCookie('csrftoken')},
            success: function() {
                $(div).css("background-color",color);
            }
        })
}

// $('.canvas').click(function() {
//     console.log("clicked")
// })

$(document).ready(function() {
    $('.canvas').click(function() {
    console.log("clicked")
    })
    $('.canvas').on('dragenter', function(){
        console.log("drag enter")
        var x = this.id.split('-')[0];
        var y = this.id.split('-')[1];
        draw(x, y, window.color, this);
    });
    $('.canvas').on('dragleave', function(){
        console.log("drag leave")
        var x = this.id.split('-')[0];
        var y = this.id.split('-')[1];
        draw(x, y, window.color, this);
    });
})


// $("#canvas").mousedown(function(){
//     ctx.beginPath();


// })

// $("#myCanvas").mouseup(function(){
    
// })


// $('#canvas').on('dragenter', function(){
//         $(this).addClass('drag-over');
// });
// $('#canvas').on('dragleave', function(){



// function write (){
//     var canvas = document.getElementById('canvas');
//     var ctx = canvas.getContext('2d');






// $(document).ready(function() {
//   $("#Post").click(function(){
//     // console.log("in ajax")
//       $.ajax({
//         url: "/db/",
//         type: "post",
//         data: {'text': $("#PostContent").val(), 'RoomID' : window.roomID, csrfmiddlewaretoken: getCookie('csrftoken')},
//         success: function(result){
//             postText = $("#PostContent").val()
//             postelement = "<p class='postlist' align='center'>" + postText + "</p>"
//             $("#posthere").append(postelement);
//           }
//       });
//     });

//   $("body").on("click","#newroombutton",function() {
//     $.ajax({
//         url: createRoomURL,
//         type: "post",
//         success: function(result) {
//             var atags = '';
//             for (var i = 0; i < result["roomIDs"].length; i++) {
//                 id = result["roomIDs"][i];
//                 atags = atags + "<a href=\"" + homepageRedirectURL + id + "/\"> Room" +  id + "</a>";
//             }
//             atags = atags + '<a id="newroombutton"> New Room</a>';
//             $("#dropdownmenu").html(atags);
//         }
//     })


//   });
}

