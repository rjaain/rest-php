<?php

function exit_with_err($err_msg)
{
  echo $err_msg;
  exit(1);
}

function handle_get()
{
  foreach( $x in $_GET)
  {
    print($x'--'$_GET["$x"]);
  }
}

function handle_post()
{
  foreach( $x in $_POST)
  {
    print($x'--'$_POST["$x"]);
  }
}

function handle_put()
{
  readfile('php://input');
}

function handle_delete()
{
  readfile('php://input');
}

switch($_SERVER['REQUEST_METHOD'])
{
  case 'GET' : 
  handle_get();
  break;
  case 'POST' : 
  handle_post();
  beak;
  case 'PUT' :
  handle_put();
  break;
  case 'DELETE' :
  handle_delete();
  break;
  default :
  exit_with_err('ERROR: Uknown Requet Header');
  }
  
  ?>
  
  
