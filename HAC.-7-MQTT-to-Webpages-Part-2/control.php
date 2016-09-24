<?php if($run!='test:code'){die();} ?>
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Control</title>
<script language="javascript" type="text/javascript">
  function init()
  {
	doConnect();
  }
  function doConnect()
  {
    websocket = new WebSocket("ws://"+document.domain+":8080/");
    websocket.onopen = function(evt) { onOpen(evt) };
    websocket.onclose = function(evt) { onClose(evt) };
    websocket.onmessage = function(evt) { onMessage(evt) };
    websocket.onerror = function(evt) { onError(evt) };
  }
  function onOpen(evt)
  {
    console.log("connected\n");
  }
  function onClose(evt)
  {
    console.log("disconnected\n");
  }
  function onMessage(evt)
  {
    console.log(evt.data);
  	var obj = JSON.parse(evt.data);
    if(obj['mode']=="login"){
		  websocket.send('{"mode": "login", "ws_token":"<?php echo $_SESSION["WS_TOKEN"]; ?>"}');
	  }else{
	    
	  }
  }
  function onError(evt)
  {
    console.log("ERROR");
	  websocket.close();
  }
  window.addEventListener("load", init, false);
  function sendSub() {
       var array_temp={};
       array_temp['mode']="subscribe";
       array_temp['topic']=document.myform.inputtextSub.value;
       websocket.send(JSON.stringify(array_temp));
   }
   function sendPub() {
       var array_temp={};
       array_temp['mode']="publish";
       array_temp['topic']=document.myform.inputtextPubTopic.value ;
       array_temp['message']=document.myform.inputtextPub.value ;
       websocket.send(JSON.stringify(array_temp));
   }
</script>
</head>

<body>
Control<br>
<a href="/?p=logout">Log Out</a>




</form>
</body>
</html>
