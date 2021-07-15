$(window).load(function() {
  // Animate loader off screen
  $(".spinner-wrapper").fadeOut("slow");
  });





/*


$(document).ready(function(){
  $('button').click(function(){
    alert("Your file uploaded successfully!");
  });
  });

<div class='spinner-wrapper'>
<div class="spinner"></div>
</div>


<let spinnerWrapper = document.querySelector('.spinner-wrapper');

window.addEventListener('load', function () {
// spinnerWrapper.style.display = 'none';
spinnerWrapper.parentElement.removeChild(spinnerWrapper);
});


$(window).load(function() {
// Animate loader off screen
$(".spinner-wrapper").fadeOut("slow");;
});


<script>
$(document).ready(function(){
  $('button').click(function(){
    $('button').parent().addClass('active');
    setTimeout(function(){
      $('button').addClass('success');
    }, 3400);
    setTimeout(function(){
      alert("Your file uploaded successfully!");
      $('button').parent().removeClass('active');
      $('button').removeClass('success');
    }, 4200);
  });
});
</script>
*/