/**
 * Function to get the static data during the page load event.
 * Gets all the static data entered by admin.
 */

$(document).ready(function(){
    var moviedata;

    /*
     * Jquery to get the static movie data
    */
    $.getJSON('movieData',{},function(data){
      movieData = data;
      var movieNames = [];
      for(var i in data){
         movieNames.push(data[i].name);
      }
      
      /*
       * Jquery plugin to autocompelte the movie phrase
      */
      $("#movies").autocomplete({
        source: movieNames,
        minLength: 2
      });
    });

    /*
     * Jquery to populate the detailes of the selected movie.
    */
    $("#details").click(function(){
       for(var i in movieData){
          if(movieData[i].name == $("#movies").val()){
             $('#name').html(movieData[i].name);
             $('#score').html(movieData[i].imdb_score);
             $('#popularity').html(movieData[i].popularity);
             $('#director').html(movieData[i].director);
             return;
          }
       }
       
    });
}); 


