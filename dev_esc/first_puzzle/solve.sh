#!/usr/bin/env sh

ENDPOINT='link_puzzle/promo'

while true
do
	for x in {a..z}
	do
		ENDPOINT_TEST="${ENDPOINT}/$x"
		
		RESP_CODE=$(curl -I -L --silent https://www.dev-esc.com/$ENDPOINT_TEST | grep "HTTP*" | tail -n 1 | cut -d$' ' -f2)

		if [ $RESP_CODE -eq 200 ] 
		then
			ENDPOINT=$ENDPOINT_TEST
			ECHO $ENDPOINT
			break
		elif [ ${x} == z ] && [ $RESP_CODE -eq 404 ]
		then
			exit 0
		fi
	done
done
