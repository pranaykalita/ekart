$(document).ready(function() {
  $('table#dataTable').DataTable();
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

//SKU GENERATE on Selleer
$(document).ready(function() {
  $('#generate-sku').click(function() {
    const charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let sku = 'SKU-'+'';
    for (let i = 0; i < 8; i++) {
      sku += charset.charAt(Math.floor(Math.random() * charset.length));
    }
    $('#ProductSku').val(sku);
  });
});
