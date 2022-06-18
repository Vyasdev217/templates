<?php
# Fetch book details from isbn
function get_book_details($isbn){
  return file_get_contents('https://www.googleapis.com/books/v1/volumes?q='.$isbn.'+isbn');
  //$str = json_decode($json, true);
  //echo '<pre>' . print_r($str, true) . '</pre>';
}
?>
