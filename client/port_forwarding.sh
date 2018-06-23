python configure.py
auth_token=$(jq '.auth_tok' ~/.mrmark_config.json)
echo "$(tput setaf 1)******Please note your authentication token - $auth_token******$(tput sgr 0)" && \
ssh -T -o StrictHostKeyChecking=no -R $(eval printf '%s' $auth_token):80:localhost:7777 serveo.net 
# ssh -o StrictHostKeyChecking=no -R 80:localhost:7777 -p 2222 $(eval printf '%s' $auth_token)@ssh.localhost.run
