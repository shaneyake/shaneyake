#Hello, This folder is for my Video HAC. 7 MQTT to webpages.

#I want to start of by saying thanks to https://github.com/dpallot/simple-websocket-server for making this possible.
#
#This MQTT to Websocket bridge uses tokens to authenticate and because of that can't be run alone, it needs a webserver to work. You will also nedd the following MQYSQL TABLES.

CREATE TABLE IF NOT EXISTS accounts ( id int(10) NOT NULL, username varchar(150) NOT NULL, password varchar(150) NOT NULL, md5_username varchar(150) NOT NULL, email varchar(150) NOT NULL, login_period int(3) NOT NULL DEFAULT '30' ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1; ALTER TABLE accounts ADD PRIMARY KEY (id); ALTER TABLE accounts MODIFY id int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=0;

CREATE TABLE IF NOT EXISTS logins ( id int(100) NOT NULL, md5_username varchar(100) NOT NULL, WS_token varchar(100) NOT NULL, expiry_date varchar(100) NOT NULL, active int(1) NOT NULL DEFAULT '0' ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1; ALTER TABLE logins ADD PRIMARY KEY (id); ALTER TABLE logins MODIFY id int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=0;

CREATE TABLE IF NOT EXISTS websockets_acls ( id int(11) NOT NULL, username varchar(100) NOT NULL, topic varchar(256) NOT NULL, rw int(1) NOT NULL DEFAULT '1') ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1; ALTER TABLE websockets_acls ADD PRIMARY KEY (id); ALTER TABLE websockets_acls MODIFY id int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=0;

CREATE TABLE IF NOT EXISTS websockets_conlist ( id int(10) NOT NULL, connections_id bigint(100) NOT NULL, username_md5 varchar(32) NOT NULL, connected int(1) NOT NULL, logged_in int(1) NOT NULL DEFAULT '0', IP varchar(100) NOT NULL, timestamp timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1; ALTER TABLE websockets_conlist ADD PRIMARY KEY (id); ALTER TABLE websockets_conlist MODIFY id int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=0;

CREATE TABLE IF NOT EXISTS websockets_topics ( id int(10) NOT NULL, connections_id bigint(100) NOT NULL, topic1 varchar(1000) NOT NULL, topic2 varchar(1000) NOT NULL, topic3 varchar(1000) NOT NULL, topic4 varchar(1000) NOT NULL, topic5 varchar(1000) NOT NULL, topic6 varchar(1000) NOT NULL, topic7 varchar(1000) NOT NULL, topic8 varchar(1000) NOT NULL, topic9 varchar(1000) NOT NULL, topic10 varchar(1000) NOT NULL ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1; ALTER TABLE websockets_topics ADD PRIMARY KEY (id); ALTER TABLE websockets_topics MODIFY id int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=0;


