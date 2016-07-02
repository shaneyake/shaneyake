<?php if($run!='test:code'){die();} ?>
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Login</title>
</head>

<body>
<form action="/?p=login_proccess" method="post">
login:<br>
<input type="text" name="usr"/><br>
<input type="password" name="pwd"/><br>
<input type="submit" value="Login"/>
</form>
</body>
</html>
