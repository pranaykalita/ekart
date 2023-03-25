//datatable
$(document).ready(function () {
    $('table#TableStyle').DataTable();
});

//CategoryEdit Disable on ADd SUbCategoryBtn MODAL
$(document).ready(function() {
  // Disable the input field if the disabled option is selected
  if ($('#pickCategory option:selected').is(':disabled')) {
    $('#subcategoryInput').prop('disabled', true);
  }

  $('#pickCategory').change(function() {
    if ($('#pickCategory option:selected').val() !== "selecteddisable") {
    console.log("pass")
      $('#subcategoryInput').prop('disabled', false);
    } else {
    console.log("fail")
      $('#subcategoryInput').prop('disabled', true);
    }
  });
});
