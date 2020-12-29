$('.demo-text-input').keyup(updateCount);
$('.demo-text-input').keydown(updateCount);

function updateCount() {
var cs = [$(this).val().length];
$('.characters').text(cs);
}