<?php if($run!='test:code'){die();} ?>
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Dashboard</title>
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
    writeToScreen("connected\n");
  }
  function onClose(evt)
  {
    writeToScreen("disconnected\n");
  }
  function onMessage(evt)
  {
    console.log(evt.data);
	writeToScreen("response: " + evt.data + '\n');
	var obj = JSON.parse(evt.data);
    if(obj['mode']=="login"){
		doSend('{"mode": "login", "ws_token":"<?php echo $_SESSION["WS_TOKEN"]; ?>"}');
	}else{
	    
	}
  }
  function onError(evt)
  {
    writeToScreen('error: ' + evt.data + '\n');
	websocket.close();
  }
  function doSend(message)
  {
    writeToScreen("sent: " + message + '\n'); 
    websocket.send(message);
  }
  function writeToScreen(message)
  {
    document.myform.outputtext.value += message
	document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;
  }
  window.addEventListener("load", init, false);
  function sendSub() {
       var array_temp={};
       array_temp['mode']="subscribe";
       array_temp['topic']=document.myform.inputtextSub.value;
       doSend(JSON.stringify(array_temp));
   }
   function sendPub() {
       var array_temp={};
       array_temp['mode']="publish";
       array_temp['topic']=document.myform.inputtextPubTopic.value ;
       array_temp['message']=document.myform.inputtextPub.value ;
       doSend(JSON.stringify(array_temp));
   }
  function clearText() {
		document.myform.outputtext.value = "";
   }
   function doDisconnect() {
		websocket.close();
   }
</script>
</head>

<body>
Dashboard<br>
<a href="/?p=logout">Log Out</a>
<div id="output"></div>

<form name="myform">
<p>
<textarea name="outputtext" rows="20" cols="100"></textarea>
</p>
Subscribe
<p>
<textarea name="inputtextSub" cols="50"></textarea><input type="button" name=sendButton value="Send" onClick="sendSub();" style="height: 36px;    top: -14px;    position: relative;">
</p>
Publish
<p>
<textarea name="inputtextPubTopic" cols="50"></textarea><textarea name="inputtextPub" cols="50"></textarea><input type="button" name=sendButton value="Send" onClick="sendPub();" style="height: 36px;    top: -14px;    position: relative;">
</p>
<p>
<input type="button" name=clearButton value="Clear" onClick="clearText();">
<input type="button" name=disconnectButton value="Disconnect" onClick="doDisconnect();">
<input type="button" name=connectButton value="Connect" onClick="doConnect();">
</p>


</form>
</body>
</html>
