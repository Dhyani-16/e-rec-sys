 // increment quantity when btn + btn clicked
 document.getElementById('increment').addEventListener('click',function () {

    let quantity = document.getElementById('quantity');
    innernumber = quantity.innerText;
    innernumber = parseInt(innernumber,10);
    innernumber++;
    quantity.innerText = innernumber;

})
// decrement quantity when btn + btn clicked
document.getElementById('decrement').addEventListener('click',function () {

    let quantity = document.getElementById('quantity');
    innernumber = quantity.innerText;
    innernumber = parseInt(innernumber,10);
    if (innernumber > 0){
        innernumber--;
    }
    quantity.innerText = innernumber;

})

function addtowishlist() {

    let heart = document.getElementById('wishlist')
    if (heart.style.color =='gray'){

    heart.style.color = 'red'
    }
    else{
        heart.style.color = 'gray'
    }

}

// function make_it_orange(id) {

//     let e = document.getElementById(id)
//     if (e.style.color != 'orange') {
//         e.style.color = 'orange'
//     }

// }

// $('#star1,#star2,#star3,#star4,#star5').hover(function (e) {
//     onid = e.target.id
//     num = parseInt(onid[4])

//     for (let i = 1; i <= num; i++) {
//         id = 'star' + i.toString()
//         make_it_orange(id)
//     }
// }, function () {
//     for (let i = 1; i <= 5; i++) {
//         id = 'star' + i.toString()
//         let e = document.getElementById(id)
//         e.style.color = 'black'
//     }
// })

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" w3-white", "");
  }
  x[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " w3-white";
}

document.getElementById('button').addEventListener("click", function() {
document.querySelector('.bg-modal').style.display = "flex";
});

// document.querySelector('.close').addEventListener("click", function() {
// document.querySelector('.bg-modal').style.display = "none";
// });


// function emoji(id) {

//     e = document.getElementById(id);
//     e.style.fontSize = '3rem'
//     console.log(e.style.fontSize);
// }

let star_status = 0; 
$('#emoji1 , #emoji2 , #emoji3 , #emoji4 , #emoji5').hover(function (e) {

    let t = e.target;
    t.style.transition = "all 0.5s"
    t.style.fontSize = '3rem';
    t.style.cursor = "pointer"
    let cl = document.getElementById(t.id).addEventListener('click',function (e1) {
        temp = t.id[5]
        star_status = parseInt(temp)
        console.log(star_status);
        
    })
    
    
},
    function (e) {
    
        let t = e.target;
        t.style.fontSize = '2.5rem';
    
    })