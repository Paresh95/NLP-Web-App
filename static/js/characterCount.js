// $('.demo-text-input').keyup(updateCount);
// $('.demo-text-input').keydown(updateCount);

// function updateCount() {
// var cs = [$(this).val().length];
// $('.characters').text(cs);
// }

$(".demo-text-input").on('input click', function(){
    $(".characters").text($(this).val().length);
  });


