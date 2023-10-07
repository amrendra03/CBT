// alert button ----------------------

function alertCopy() {
    alert('Copy Successfully.');
};


// popup window ------------------
// var flag = 0;
function openPopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "block";
    // flag = 1;
}

function closePopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "none";
    console.log(flag);
}

// const popupContainer = document.getElementById("popupContainer");


// document.addEventListener("click", function (event) {
//     if (event.target !== popupContainer && !popupContainer.contains(event.target)) {
//         closePopup();
//     }
// });



