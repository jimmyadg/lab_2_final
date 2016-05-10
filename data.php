<?php

$host = 'localhost';
$user = 'root';
$pass = 'toor';

@mysql_connect($host,$user,$pass) or die('Connection failed');
@mysql_select_db('cycle');
//echo 'good';

$sql = mysql_query("SELECT * FROM data ORDER BY ID ASC");
$id = 'ID';
$date = 'Date';
$Time = 'Time';
$status = 'Status';
$position = 'Position';

 ?>

<html>
<head>
  <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600' rel='stylesheet' type='text/css' >
<style>
body{
  font-family: 'Open Sans' ,sans-serif;
  font-size: 60px;
  background: #99CCFF;
}
h1{
  margin: 23% auto;
  text-align: center;
  color: white;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: black;
  font-size: 90px;
}
.header{
  display: inline-block;
  margin: 5% 0 0 28%;

}
div{
  display: inline-block;
  margin: 5% 1% 8% 32%;
}
</style>
</head>
<body>
  <h1>Biological Clock Cycle</h1>
  <div class="head">
    Start:
  </div>
  <div class="head">
    Stop:
  </div>
  <?php
while($rec=mysql_fetch_assoc($sql)){
  echo "<div>";
  echo $rec[$position];
  echo "</div>";
}
  ?>
</body>
</html>
 
