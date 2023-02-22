<?php
session_start();
$db = mysqli_connect('localhost', 'kokurou', 'sequeladmin', 'phishing')or die("Not connecting");
$username =$_POST['uname'];
$password =$_POST['psw'];
$sql = "SELECT * FROM `admin` WHERE `alloted_id`='$username' AND password='$password' " ;
$results = mysqli_query($db, $sql);
if (mysqli_num_rows($results) == 1) 
{
	
	$_SESSION['username'] = $username;
	echo "<script>alert('YOU ARE NOW LOGGED IN');</script>";
	echo "<script>window.location='admindash.php';</script>";
	exit;
}
else 
{
	
	echo "<script>window.location='index.php?message=Incorrect Username or Password';</script>";
}
?>