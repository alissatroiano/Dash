 // jQuery
 $(document).ready(function() {
     $('.sidenav').sidenav({
         edge: "right"
     });
     $('.fixed-action-btn').floatingActionButton();
     $('.waves-effect.waves-light').floatingActionButton();
     $('.tooltipped').tooltip();
 });

 $(function() {
     $('#delete-recipe').click(function() {
         let confirm = confirm("Are you sure?");
         if (confirm == true) {
             $.ajax({
                 url: '/recipes/{{row[0]}}',

                 success: function(response) {
                     console.log(response);
                 },
                 error: function(error) {
                     console.log(error);
                 }
             });

         } else {

         }
     });

 });