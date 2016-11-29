<?php // login.php
  $hn = 'localhost';
  $db = 'teachers_library';
  $un = 'root';
  $pw = '';
?>
import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = " ",
                           db = "teachers_library")
    c = conn.cursor()

    return c, conn
		