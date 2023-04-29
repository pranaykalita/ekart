$(document).ready(function() {
  $('table#dataTable').DataTable({
  });
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


//check category if already avail in database
$(document).ready(function() {
    // check if Category is available
    $('#insertcategory').on('change keyup blur', function() {
        var category = $(this).val();
        $.ajax({
            url: '/api/categorylist/',
            type: 'GET',
            data: {category: category},
            success: function(response)
            {
            if(response[0].categoryName == category)
            {
            console.log("Not Available")
            $('#caterror').text('Category already Available.');
            $('#savecategorybtn').prop('disabled', true);
            }
            else{
            $('#caterror').text('');
            $('#savecategorybtn').prop('disabled', false);
            }
            }
        });
    });
    // check if Subcategory is available
    $('#subcategoryInput').on('change keyup blur', function() {
        var subcategory = $(this).val();
        $.ajax({
            url: '/api/categorylist/',
            type: 'GET',
            data: {subcategory: subcategory},
            success: function(response)
            {
            if(response[0].subcategories[0].subcatgName == subcategory)
            {
            console.log("Not Available")
            $('#subcaterror').text('Subcategory already Available.');
            $('#savesubcategorybtn').prop('disabled', true);
            }
            else{
            $('#subcaterror').text('');
            $('#savesubcategorybtn').prop('disabled', false);
            }
            }
        });
    });


});
