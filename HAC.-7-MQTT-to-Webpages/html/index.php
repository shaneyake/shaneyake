hi
<?php
session_start();$run='test:code';
$MYSQL_SERVER='';
$MYSQL_USERNAME='';
$MYSQL_PASSWORD='';
$MYSQL_DATABASE='';

$page='dashboard';
if($_SESSION["USER_VAILD"] == "vaild"){
	if($_GET['p']!=''){$page=$_GET['p'];}
}else{
	$page="login";
    if($_GET['p']=='login_proccess'){$page='login_proccess';}
}
include $page.'.php';
?>