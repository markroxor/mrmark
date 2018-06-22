python configure.py
auth_token=$(jq '.auth_key' ~/.mrmark_config.json)
# ssh -o StrictHostKeyChecking=no -R 80:localhost:7777 -p 2222 $(eval printf '%s'2 $auth_token)@ssh.localhost.run
ssh -o StrictHostKeyChecking=no -R $(eval printf '%s' $auth_token):80:localhost:7777 serveo.net