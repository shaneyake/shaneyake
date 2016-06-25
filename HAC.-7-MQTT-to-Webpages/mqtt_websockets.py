#Imports
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
import signal, sys, logging
from optparse import OptionParser
import MySQLdb as mdb
import string
import datetime
import time
import thread
import json
from collections import defaultdict
import paho.mqtt.client as mqtt


websockets_port=#WEBSOCKETS_PORT#

mqtt_server="#MQTT_SERVER#"
mqtt_port=#MQTT_PORT#
mqtt_username="#MQTT_USERNAME#"
mqtt_password="#MQTT_PASSWORD#"


mysql_db='#MYSQL_DB#'
mysql_username='#MYSQL_USERNAME#'
mysql_password='#MYSQL_PASSWORD#'
mysql_server='#MYSQL_SERVER#'

#Variables
var_connections_id = {}
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
#Mysql
class DB:
    conn = None
    
    def connect(self):
        self.conn = mdb.connect(mysql_server, mysql_username, mysql_password, mysql_db)
        self.conn.autocommit(True)
        print("MySQL Connected")
    
    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except (AttributeError, mdb.OperationalError):
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
        return cursor

db = DB()
db.connect()
db2 = DB()
db2.connect()
db3 = DB()
db3.connect()
db4 = DB()
db4.connect()

#MQTT on connect callback
def on_connect(mqttc, userdata, flags, rc):
    print("MQTT Connected...")
#MQTT on message callback
def on_message(mqttc, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    global var_connections_id
    msg_topic_sql={}
    msg_topic_sql[0]=""
    msg_topic_sql[1]=""
    msg_topic_sql[2]=""
    msg_topic_sql[3]=""
    msg_topic_sql[4]=""
    msg_topic_sql[5]=""
    msg_topic_sql[6]=""
    msg_topic_sql[7]=""
    msg_topic_sql[8]=""
    msg_topic_sql[9]=""
    temp_msg_topic = string.split(str(msg.topic),'/')
    for i in range(len(temp_msg_topic)):
        msg_topic_sql[i]=temp_msg_topic[i]
    sql4 ="SELECT `connections_id` FROM `websockets_topics` WHERE (`topic1`='"+str(msg_topic_sql[0])+"') AND `topic2`='"+str(msg_topic_sql[1])+"' AND `topic3`='"+str(msg_topic_sql[2])+"' AND `topic4`='"+str(msg_topic_sql[3])+"' AND `topic5`='"+str(msg_topic_sql[4])+"' AND `topic6`='"+str(msg_topic_sql[5])+"' AND `topic7`='"+str(msg_topic_sql[6])+"' AND `topic8`='"+str(msg_topic_sql[7])+"' AND `topic9`='"+str(msg_topic_sql[8])+"' AND `topic10`='"+str(msg_topic_sql[9])+"';"
    cur4 = db4.query(sql4)
    numrows4 = int(cur4.rowcount)
    if(numrows4>=1):
        results = cur4.fetchall()
        for row in results:
            try:
                temp_id =row[0]
                client=var_connections_id[temp_id][0]
                temp_send_ws={}
                temp_send_ws['topic']=str(msg.topic)
                #temp_send_ws['message']=str(msg.payload)
                temp_send_ws['message']=msg.payload.decode("UTF-8")
                temp_send_ws['mode']="mqtt"
                print(msg.payload.decode("UTF-8"))
                print(msg.payload.decode("UTF-8"))
                print(str(json.dumps(temp_send_ws)))
                client.sendMessage(str(json.dumps(temp_send_ws)))
            except Exception as n:
                print(n)

#MQTT Client Function
def start_mqtt():
    global mqttc
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.username_pw_set(mqtt_username, mqtt_password)s
    mqttc.connect(mqtt_server, mqtt_port, 60)
    mqttc.loop_forever()

thread.start_new_thread( start_mqtt, (),  )

class SimpleChat(WebSocket):
    def handleMessage(self):
        if self.data is None:
            self.data = ''
        #print(self.data)
        global var_connections_id
        global delchars
        print('New Message')
        print(self.data.decode("UTF-8"))
        jason_message =json.loads(self.data.decode("UTF-8"))
        #jason_message =json.loads(str(self.data))
        print(jason_message)
        #print('Hello2')
        try:
            sql2 ="SELECT `logged_in`,`username_md5` FROM `websockets_conlist` WHERE `connections_id`='"+str(id(self))+"';"
            cur2 = db2.query(sql2)
            row2 = cur2.fetchone()
            var_loggedin=row2[0]
            var_username=row2[1]
        
        except:
            print("error")
        if (var_loggedin==1):#if Allowed
            if jason_message['mode']=="login":
                try:
                    temp_send_ws4={}
                    temp_send_ws4['mode']="system"
                    temp_send_ws4['ws_token']=jason_message['ws_token']
                    self.sendMessage(str(json.dumps(temp_send_ws4)))
                except Exception as n:
                    print(n)
            elif jason_message['mode']=="subscribe":
                var_data_on=0 
                var_temp_data = str(jason_message['topic'])
                if var_temp_data!='':
                    sql ="SELECT * FROM websockets_acls WHERE username = '"+str(var_username)+"'&&rw >= 1"
                    cur = db.query(sql)
                    numrows = int(cur.rowcount)
                    if(numrows>=1):
                        results = cur.fetchall()
                        for row in results:
                            data_topic_db = row[2]
                            data_topic_db = string.split(data_topic_db,'/')
                            data_topic_message = string.split(var_temp_data, '/')
                            if row[2]=="#":
                                var_data_on=1
                                break
                            elif row[2]==var_temp_data:
                                var_data_on=1
                                break
                            elif "guest"==data_topic_message[0]:
                                var_data_on=1
                                break                    
                    else:
                        var_data_on=0

                else:
                    var_data_on=0
                        
                if var_data_on==1:
                    msg_topic_sql={}
                    msg_topic_sql[0]=""
                    msg_topic_sql[1]=""
                    msg_topic_sql[2]=""
                    msg_topic_sql[3]=""
                    msg_topic_sql[4]=""
                    msg_topic_sql[5]=""
                    msg_topic_sql[6]=""
                    msg_topic_sql[7]=""
                    msg_topic_sql[8]=""
                    msg_topic_sql[9]=""
                    temp_msg_topic = string.split(str(var_temp_data),'/')
                    for i in range(len(temp_msg_topic)):
                        msg_topic_sql[i]=temp_msg_topic[i]
                    sql3="INSERT INTO `websockets_topics`(`id`, `connections_id`, `topic1`, `topic2`, `topic3`, `topic4`, `topic5`, `topic6`, `topic7`, `topic8`, `topic9`, `topic10`) VALUES (NULL,'"+str(id(self))+"','"+str(msg_topic_sql[0])+"','"+str(msg_topic_sql[1])+"','"+str(msg_topic_sql[2])+"','"+str(msg_topic_sql[3])+"','"+str(msg_topic_sql[4])+"','"+str(msg_topic_sql[5])+"','"+str(msg_topic_sql[6])+"','"+str(msg_topic_sql[7])+"','"+str(msg_topic_sql[8])+"','"+str(msg_topic_sql[9])+"');"
                    cur3 = db3.query(sql3)
                    mqttc.subscribe(var_temp_data)
                    print("Subcribe Topic: "+var_temp_data)
                    try:
                        temp_send_ws3={}
                        temp_send_ws3['mode']="system"
                        temp_send_ws3['status']="SUBSCRIBED_GRANTED"
                        self.sendMessage(str(json.dumps(temp_send_ws3)))
                    except:
                        print("Error")
                else:
                    try:
                        temp_send_ws3={}
                        temp_send_ws3['mode']="system"
                        temp_send_ws3['status']="SUBSCRIBED_DENIED"
                        self.sendMessage(str(json.dumps(temp_send_ws3)))
                        
                    except:
                        print("Error")
                    
            elif jason_message['mode']=="publish":
                try:
                    var_temp_data = str(jason_message['topic'])
                    var_temp_data2 = str(jason_message['message'])
                    #print(jason_message['message'])
                    #print(str(json.dumps(jason_message['message'])))
                    var_data_on=0
                    sql ="SELECT * FROM websockets_acls WHERE username = '"+str(var_username)+"'&&rw >= 2"
                    cur = db.query(sql)
                    numrows = int(cur.rowcount)
                    if(numrows>=1):
                        if var_temp_data!='':
                            results = cur.fetchall()
                            for row in results:
                                data_topic_db = row[2]
                                data_topic_db = string.split(data_topic_db,'/')
                                data_topic_message = string.split(var_temp_data, '/')
                                if row[2]=="#":
                                    var_data_on=1
                                    break
                                elif row[2]==var_temp_data:
                                    var_data_on=1
                                    break
                                elif "guest"==data_topic_message[0]:
                                    var_data_on=1
                                    break

                    if(var_data_on==1):
                        print("Published: "+var_temp_data)
                        try:
                            temp_send_ws3={}
                            temp_send_ws3['mode']="system"
                            temp_send_ws3['status']="PUBLISHED_GRANTED"
                            self.sendMessage(str(json.dumps(temp_send_ws3)))
                            mqttc.publish(var_temp_data, str(json.dumps(jason_message['message'])))
                        except:
                            print("Error")
                    else:
                        try:
                            temp_send_ws3={}
                            temp_send_ws3['mode']="system"
                            temp_send_ws3['status']="PUBLISHED_DENIED"
                            self.sendMessage(str(json.dumps(temp_send_ws3)))
                        except:
                            print("Error")
                except Exception as n: #elif "#topic#:"
                    print n
                    print ("Error elif #topic#:")
            else:
                print("Error"+str(self.data))
        if (var_loggedin==0): #if busy
            sent=0
            if jason_message["mode"]=="login":
                var_temp_data = str(jason_message['ws_token'])
                var_sql_q = var_temp_data.translate(None, delchars)
                sql ="SELECT * FROM logins WHERE WS_token = '"+var_sql_q+"'&&active = 1"
                cur = db.query(sql)
                numrows = int(cur.rowcount)
                if(numrows==1):
                    row = cur.fetchone()
                    if(row[7]>=time.strftime('%Y-%m-%d %H:%M:%S') and row[8]==1):
                        print("Allowed " + str(id(self)))
                        print("IP: " + str(self.address[0]))
                        
                        sql ="UPDATE `websockets_conlist` SET `username_md5`='"+str(row[1])+"',`logged_in`=1 WHERE `connections_id`='"+str(id(self))+"';"
                        cur2 = db2.query(sql)
                        try:
                            temp_send_ws3={}
                            temp_send_ws3['mode']="system"
                            temp_send_ws3['status']="ACCESS_GRANTED"
                            self.sendMessage(str(json.dumps(temp_send_ws3)))
                            sent=1
                        except Exception as n:
                            print(n)
                        
                    else:
                    #print "NOOPE"
                        try:
                            temp_send_ws3={}
                            temp_send_ws3['mode']="system"
                            temp_send_ws3['status']="ACCESS_DENIED"
                            self.sendMessage(str(json.dumps(temp_send_ws3)))
                            sent=1
                        except Exception as n:
                            print(n)
            
    def handleConnected(self):
        print("Connected " + str(self))
        global var_connections_id
        #Make Sure no old rows
        sql ="DELETE FROM `websockets_conlist` WHERE `websockets_conlist`.`connections_id`='"+str(id(self))+"';"
        cur2 = db2.query(sql)
        print (id(self))
        print (var_connections_id)
        sql ="INSERT INTO `websockets_conlist` (`id`, `connections_id`, `username_md5`, `connected`,`IP`) VALUES (NULL, '"+str(id(self))+"', '', '1','"+str(self.address[0])+"');"
        cur2 = db2.query(sql)
        if id(self) in var_connections_id:
            del var_connections_id[id(self)]
            print("Deleted: var_connections_id")
        var_connections_id[id(self)]=[]
        var_connections_id[id(self)].append(self)
        print("Connected FOR GOOD")
        try:
            temp_send_ws2={}
            temp_send_ws2['mode']="login"
            self.sendMessage(str(json.dumps(temp_send_ws2)))
        except Exception as n:
            print(n)

    def handleClose(self):
        print("Closed " + str(self))
        global var_connections_id
        sql ="DELETE FROM `websockets_conlist` WHERE `websockets_conlist`.`connections_id`='"+str(id(self))+"';"
        cur2 = db2.query(sql)
        sql ="DELETE FROM `websockets_topics` WHERE `websockets_topics`.`connections_id`='"+str(id(self))+"';"
        cur2 = db2.query(sql)
        if id(self) in var_connections_id:
            del var_connections_id[id(self)]
        print(var_connections_id)
        print("Closed FOR GOOD")

if __name__ == "__main__":

   cls = SimpleChat
   server = SimpleWebSocketServer('', websockets_port, cls)
 

   def close_sig_handler(signal, frame):
      server.close()
      sys.exit()

   signal.signal(signal.SIGINT, close_sig_handler)

   server.serveforever()
