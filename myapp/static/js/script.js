let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');
let header = document.querySelector('.header-3');
let scrollTop = document.querySelector('.scroll-top');

menu.addEventListener('click', () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

window.onscroll = () => {

    menu.classList.remove('fa-times');
    navbar.classList.remove('active');

    if (window.scrollY > 250) {
        header.classList.add('active');
    } else {
        header.classList.remove('active');
    }

    if (window.scrollY > 250) {
        scrollTop.style.display = 'initial';
    } else {
        scrollTop.style.display = 'none';
    }

}

var swiper = new Swiper(".home-slider", {
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    loop: true,
});

setInterval(function () {
    countDown();
}, 1000)


$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.remove()
        }
    })
})


// Get the modal
var Omodal = document.getElementById("myOModal");

// Get the button that opens the modal
var Obtn = document.getElementById("myOBtn");

// Get the <span> element that closes the modal
var Ospan = document.getElementsByClassName("oclose")[0];

// When the user clicks the button, open the modal 
Obtn.onclick = function () {
    Omodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
Ospan.onclick = function () {
    Omodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == Omodal) {
        Omodal.style.display = "none";
    }
}

// Get the modal
var Exmodal = document.getElementById("myExModal");

// Get the button that opens the modal
var Exbtn = document.getElementById("myExBtn");

// Get the <span> element that closes the modal
var Exspan = document.getElementsByClassName("exclose")[0];

// When the user clicks the button, open the modal 
Exbtn.onclick = function () {
    Exmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
Exspan.onclick = function () {
    Exmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == Exmodal) {
        Exmodal.style.display = "none";
    }
}


// let modalBtn = document.getElementById("modal-btn")
// let modal = document.querySelector(".modal")
// let closeBtn = document.querySelector(".close-btn")
// modalBtn.onclick = function(){
//   modal.style.display = "block"
// }
// closeBtn.onclick = function(){
//   modal.style.display = "none"
// }
// window.onclick = function(e){
//   if(e.target == modal){
//     modal.style.display = "none"
//   }
// }


// $("#ex1-open").on("click", function () {
//     $(".popup-overlay, .popup-content").addClass("active");
// });

// $("#ex1-close, .popup-overlay").on("click", function () {
//     $(".popup-overlay, .popup-content").removeClass("active");
// });

// $("#ex2-open").on("click", function () {
//     $(".popup-overlay, .popup-content").addClass("active");
// });

// $("#ex2-close, .popup-overlay").on("click", function () {
//     $(".popup-overlay, .popup-content").removeClass("active");
// });



$("#w0-open").on("click", function () {
    $("#w0-modal").addClass("active");
});

$("#w0-close").on("click", function () {
    $("#w0-modal").removeClass("active");
});

$("#w1-open").on("click", function () {
    $("#w1-modal").addClass("active");
});

$("#w1-close").on("click", function () {
    $("#w1-modal").removeClass("active");
});

$("#w2-open").on("click", function () {
    $("#w2-modal").addClass("active");
});

$("#w2-close").on("click", function () {
    $("#w2-modal").removeClass("active");
});

$("#w3-open").on("click", function () {
    $("#w3-modal").addClass("active");
});

$("#w3-close").on("click", function () {
    $("#w3-modal").removeClass("active");
});

$("#w4-open").on("click", function () {
    $("#w4-modal").addClass("active");
});

$("#w4-close").on("click", function () {
    $("#w4-modal").removeClass("active");
});

$("#w5-open").on("click", function () {
    $("#w5-modal").addClass("active");
});

$("#w5-close").on("click", function () {
    $("#w5-modal").removeClass("active");
});

$("#w6-open").on("click", function () {
    $("#w6-modal").addClass("active");
});

$("#w6-close").on("click", function () {
    $("#w6-modal").removeClass("active");
});

$("#w7-open").on("click", function () {
    $("#w7-modal").addClass("active");
});

$("#w7-close").on("click", function () {
    $("#w7-modal").removeClass("active");
});

$("#w8-open").on("click", function () {
    $("#w8-modal").addClass("active");
});

$("#w8-close").on("click", function () {
    $("#w8-modal").removeClass("active");
});
