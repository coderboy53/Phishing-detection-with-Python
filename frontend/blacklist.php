<?php
$db = mysqli_connect('localhost', 'kokurou', 'sequeladmin', 'phishing')or die("Not connecting");
$url =$_POST['url'];
$q="INSERT INTO `websites` (websitename) VALUES ('$url')";
$r=mysqli_query($db,$q);
if($r){	
		echo "<script>window.location='admindash.php?message=Added successfully';</script>";
	  }
else{
	 echo mysqli_error($connect)."<br>query:".$q;
    }

?>
