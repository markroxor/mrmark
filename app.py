import requests
from flask import Flask, request, jsonify
import json
import time, os
import psycopg2

app = Flask(__name__)
config_table = 'user_config'
query_table = 'unresponsed_queries'


def database_do(action='None', userid='None', auth_key='None', mail_id='None', query='None'):
    try:
        con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')   
        cur = con.cursor()

        if action == 'get_auth':
            cur.execute("SELECT * FROM "+ config_table +" WHERE userid = '" + userid + "'")
        
            while True:
                row = cur.fetchone()
        
                if row == None:
                    break
                auth_key = str(row[0])
                print("your auth_key is " + auth_key)

        elif action == 'update_uid':
            cur.execute("SELECT * FROM "+ config_table +" WHERE auth_key = '" + auth_key + "'")
            cur.execute("UPDATE "+ config_table +" SET userid='" + userid + "' WHERE auth_key='" + auth_key + "'")
            con.commit()

        elif action == 'copy_init_config':
            cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (config_table,))

            if cur.fetchone()[0] is False:
                print("created new table named {}".format(config_table))
                cur.execute("CREATE TABLE "+ config_table +"(auth_key VARCHAR(4) PRIMARY KEY, mail_id VARCHAR(50), userid VARCHAR(200))")

            cur.execute("DELETE FROM "+ config_table +" WHERE mail_id='" + mail_id + "'") 
                
            cur.execute("INSERT INTO "+ config_table +" VALUES('" + auth_key + "','" +  mail_id + "','None')")
            con.commit()

        elif action == 'unresponsed_query':
            cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (config_table,))

            if cur.fetchone()[0] is False:
                print("created new table named {}".format(query_table))
                cur.execute("CREATE TABLE " + query_table + "(query VARCHAR(500) PRIMARY KEY)")
                
            cur.execute("INSERT INTO " + query_table + " VALUES('" + query + "')")
            con.commit()
    
    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
    
        print ('Error %s' % e  )  
    
    finally:   
        if con:
            con.close()
            
            if action == 'get_auth':
                return auth_key


@app.route("/", methods=["POST", "GET"])
def process_df_api():

    # get dialog-flow's POST request and send a POST request to the client side.
    if request.method == "POST":
        r = "GOT a DF API POST request."
        json_request = request.get_json()
        print(json_request)

        if json_request['queryResult']['action'] == 'input.unknown':
            database_do(action='unresponsed_query', query=json_request['queryResult']['queryText'])

        elif json_request['queryResult']['action'] == 'authenticate':
            auth_key = json_request['queryResult']['parameters']['auth_key']
            userid = json_request['originalDetectIntentRequest']['payload']['user']['userId']

            database_do(action='update_uid', auth_key=auth_key, userid=userid)
            print("Linked {} with {}".format(auth_key, userid))

        else:
            userid = json_request['originalDetectIntentRequest']['payload']['user']['userId']
            auth_key = database_do(action='get_auth', userid=userid)

            url = 'https://' + auth_key + '.serveo.net'
            headers = {'content-type': 'application/json'}

            print("Sending payload {} to {}".format(url, json_request))
            resp = requests.post(url=url, data=json.dumps(json_request), headers=headers)
            r = resp.text

        return r, 200
        
    if request.method == "GET":
        return "Heroku GOT a request", 200

@app.route("/config", methods=["POST"])
def process_config():

    # saves the POSTED user configuration in conf folder
    if request.method == "POST":
        print(request, "request")
        config = request.get_json()

        print(config)
        database_do(action='copy_init_config', auth_key=config['auth_key'], mail_id=config['email_id'])

        return "saved the new configuration", 200

if __name__ == '__main__':
    app.run(debug = True)