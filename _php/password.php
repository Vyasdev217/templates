<?php

# Generate password hash
function hash($password){
  password_hash($password, PASSWORD_DEFAULT);
}

# Check password
function verify_pw($password, $pw_hash){
  return password_verify($password, $pw_hash);
  # True -- Correct pw
  # False -- Wrong pw
}

?>
