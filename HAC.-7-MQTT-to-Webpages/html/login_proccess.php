<?php if($run!='test:code'){die();}
$MYSQL_SERVER='';
$MYSQL_USERNAME='';
$MYSQL_PASSWORD='';
$MYSQL_DATABASE='';

$username = $_POST['usr'];
$username = strtolower($username);
$usernamemd5=md5($username);
$password = $_POST['pwd'];
$passwordmd5=md5($password);
if ($username&&$password){ //start if 1
$conn = new mysqli($MYSQL_SERVER, $MYSQL_USERNAME, $MYSQL_PASSWORD, $MYSQL_DATABASE);
mysql_connect($MYSQL_SERVER,$MYSQL_USERNAME,$MYSQL_PASSWORD);
	@mysql_select_db($MYSQL_DATABASE) or die( "Unable to select database");

$query="SELECT * FROM accounts WHERE md5_username ='$usernamemd5'";
$result=mysql_query($query);
$numrows=mysql_numrows($result);

if ($numrows!=0){ //start if 2

 $i=0;
 while ($i < $numrows) { //start while 1
	$dbusername = mysql_result($result,$i,"username");
	$dbmd5_username = mysql_result($result,$i,"md5_username");
	$dbpassword = mysql_result($result,$i,"password");
	$dbgetid=mysql_result($result,$i,"id");
	$i++;
 }

if ($usernamemd5==$dbmd5_username&&$passwordmd5==$dbpassword) { //start if 3
	if($dbactive>='7'){
	$newkey = uniqid();
	$newkeymd5=md5($newkey);
	$WS_token = md5($dbgetid.$newkey);
	$newexpiry_date = date('Y-m-d h:i:s', time()+(86400 * 30));
	$_SESSION["USER_VAILD"]= "vaild";
	$_SESSION["USER_NAME"] = $dbusername;
	$_SESSION["USER_NAME_KEY"] = $dbmd5_username;
	$_SESSION["WS_TOKEN"] = $WS_token;
	$sql="INSERT INTO logins (id, md5_username, expiry_date, WS_token, active) VALUES (NULL, '$dbmd5_username', '$dbexpiry_date', '$WS_token' , '1' )";
	mysqli_query($conn, $sql) or die("Couldn't Create Key");
	echo("200");
	}else{echo("1");}
} else { //close if 3
	echo("2");
}

}else{//close if 2
	echo("3");
}
}else{//close if 1
	echo("4");
 }
?>
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Logging in...</title>
</head>

<body>
</body>
</html>