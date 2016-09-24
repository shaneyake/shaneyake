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
  function sendSub(topic) {
       var array_temp={};
       array_temp['mode']="subscribe";
       array_temp['topic']=topic;
       websocket.send(JSON.stringify(array_temp));
   }
   function sendPub(topic,message) {
       var array_temp={};
       array_temp['mode']="publish";
       array_temp['topic']=topic;
       array_temp['message']=message;
       websocket.send(JSON.stringify(array_temp));
   }

   function sendRGB(color,value){
       var array_temp={};
       array_temp[color]=value;
       sendPub('hello/world',array_temp);
   }

   function sendButtonPress(value){
       var array_temp={};
       array_temp['STATE']=value;
       sendPub('hello/world',array_temp);
   }
</script>
</head>

<body>
Control<br>
<a href="/?p=logout">Log Out</a>
<br>

<br>
RED___:<input type="range" id="myRange" value="90" min="0" max="255" onChange="sendRGB('RED',this.value)"><br>
GREEN:<input type="range" id="myRange" value="90" min="0" max="255" onChange="sendRGB('GREEN',this.value)"><br>
BLUE__:<input type="range" id="myRange" value="90" min="0" max="255" onChange="sendRGB('BLUE',this.value)"><br>
<br>
<button onClick="sendButtonPress(1)">ON</button><br>
<button onClick="sendButtonPress(0)">OFF</button><br>
<button onClick="sendButtonPress('T')">TOGGEL</button><br>

</body>
</html>
