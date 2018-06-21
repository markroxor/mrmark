import requests
from flask import Flask, request, jsonify
import json
import time, os
import psycopg2

username = 'mrmohitrathoremr'
config_file = 'conf.json'

app = Flask(__name__)

def authenticate_user(data):
    parameters = data['queryResult']['parameters']
    action = data['queryResult']['action']
    
    if action == 'authenticate':
        print(parameters['auth_key'])

def update_auth_key(conf, key):
    with open(config_file) as f:
        confs = json.load(f)

    username = conf['email_id'].split('@gmail.com')[0] 
    confs[username] = conf

    print(confs, config_file)
    with open(config_file, 'w') as f:
        json.dump(confs, f)


@app.route("/", methods=["POST", "GET"])
def process_df_api():

    # get dialog-flow's POST request and send a POST request to the client side.
    if request.method == "POST":
        r = "GOT a DF API POST request."
        json_request = request.get_json()
        print(json_request)

        # with open(config_file) as f:
        #     confs = json.load(f)

        # auth_token = confs[username]['auth_token']

        if json_request['queryResult']['action'] == 'input.unknown':
            with open("unresponsed_queries.txt", 'a') as js:
                js.write(json.dumps(json_request['queryResult']['queryText']) + '\n')
        elif json_request['queryResult']['action'] == 'authenticate':
            auth_key = json_request['queryResult']['parameters']['auth_key']
            userid = json_request['originalDetectIntentRequest']['payload']['user']['userId']
            print("here", auth_key, userid)
            try:
                con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')   
                cur = con.cursor()
                cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('user_config',))

                if cur.fetchone()[0] is False:
                    print("created")
                    cur.execute("CREATE TABLE user_config(auth_tok VARCHAR(4) PRIMARY KEY, mail_id VARCHAR(50), userid VARCHAR(200))")
                

                cur.execute("SELECT * FROM user_config WHERE auth_tok = '"+auth_key+"'")
                cur.execute("UPDATE user_config SET userid='"+userid+"' WHERE auth_tok='"+auth_key+"'")
                con.commit()
                
            except psycopg2.DatabaseError as e:
                if con:
                    con.rollback()
            
                print ('Error %s' % e)    
            
            finally:   
                if con:
                    con.close()  


        else:
            userid = json_request['originalDetectIntentRequest']['payload']['user']['userId']
            try:
                con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')   
                cur = con.cursor()
                cur.execute("SELECT * FROM user_config WHERE userid = '"+userid+"'")
            
                while True:
                    row = cur.fetchone()
            
                    if row == None:
                        break
                    auth_tok = str(row[0])
                    print("your auth_tok is " + auth_tok)
            
            except psycopg2.DatabaseError as e:
                if con:
                    con.rollback()
            
                print ('Error %s' % e  )  
            
            finally:   
                if con:
                    con.close()


            url = 'https://'+auth_tok+'.serveo.net'
            headers = {'content-type': 'application/json'}

            resp = requests.post(url=url, data=json.dumps(json_request), headers=headers)
            print("response", resp.text)
            r = resp.text

        # con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')   
        # cur = con.cursor()

        # cur.execute("SELECT * FROM user_config WHERE auth_tok = '3C59'")
    
        # while True:
        #     row = cur.fetchone()
    
        #     if row == None:
        #         break
    
        #     print("Mail ID: " + row[1] + "\t\tuserid: " + str(row[2]))

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

        try:
            con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')   
            cur = con.cursor()
            cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('user_config',))

            if cur.fetchone()[0] is False:
                print("created")
                cur.execute("CREATE TABLE user_config(auth_tok VARCHAR(4) PRIMARY KEY, mail_id VARCHAR(50), userid VARCHAR(200))")
                
            cur.execute("INSERT INTO user_config VALUES('"+config['auth_token']+"','"+ config['email_id']+"','None')")
            con.commit()

        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
        
            print ('Error %s' % e)    
        
        finally:   
            if con:
                con.close()

        return "saved the new configuration", 200

if __name__ == '__main__':
    app.run(debug = True)