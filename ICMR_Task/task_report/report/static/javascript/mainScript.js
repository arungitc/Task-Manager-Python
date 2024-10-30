$(document).ready(function ($) {
  $("#recordTable").DataTable({
    pagingType: "full_numbers",
    pageLength: 10,
    dom:
      "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>" +
      "<'row'<'col-sm-12'tr>>" +
      "<'row'<'col-sm-12'p>>",

    language: {
      search: "",
      searchPlaceholder: "Search records",
      
    },
    drawCallback: function () {
      var pagination = $(this)
        .closest(".dataTables_wrapper")
        .find(".dataTables_paginate");
      pagination.addClass("custom-pagination");
      pagination.find("a").wrap('<li class="page-item"></li>');
      pagination.find("span").wrap('<li class="page-item"></li>');

      pagination.find("li").click(function () {
        pagination.find("li").removeClass("active");
        $(this).addClass("active");
      });
    },
  });
});









// block right click on the webpage

// document.addEventListener('contextmenu', function(e) {
//     e.preventDefault();
//     alert('Access Denied');
//   });

//   document.onkeydown = function(e) {
//     if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74)) || (e.ctrlKey && e.keyCode === 85)) {
//       alert('Access Denied');
//       return false;
//     }
//   };




  