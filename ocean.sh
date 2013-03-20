#!/bin/bash
#digital ocean api utility
#should probably source keys from a file apikeys.conf
#rewrite in python

URL='https://api.digitalocean.com'
YOUR_CLIENT_ID=wPGMS65J51BxOTxBRM4zU
YOUR_API_KEY=cGzGiaEB86JYZbu3g5QPyjCeX9cOnc9H3ELkPzSO2
AUTH='client_id='$YOUR_CLIENT_ID'&api_key='$YOUR_API_KEY

#hnbot image
HNIMG=144609

getdrops(){
	curl -s $URL'/droplets/?'$AUTH
}

getimages(){
	if [[ $1 == all ]] ;then
		filter=global
	else
		filter=my_images
	fi
	curl -s $URL'/images/?'$AUTH'&filter='$filter
}

getkeys(){
	curl -s $URL'/ssh_keys/?'$AUTH
}

showkey(){
	chkid $1
	SSH_KEY_ID=$1
	curl -s $URL'/ssh_keys/'$SSH_KEY_ID'/?'$AUTH
}

dropstatus(){
	chkid $1
	DROPLET_ID=$1
	curl -s $URL'/droplets/'$DROPLET_ID'/?'$AUTH
}

startdrop(){
	chkid $1
	DROPLET_ID=$1
	curl -s $URL'/droplets/'$DROPLET_ID'/power_on/?'$AUTH
}

stopdrop(){
	chkid $1
	DROPLET_ID=$1
	curl -s $URL'/droplets/'$DROPLET_ID'/shutdown/?'$AUTH
}

killdrop(){
	chkid $1
	DROPLET_ID=$1
	curl -s $URL'/droplets/'$DROPLET_ID'/power_off/?'$AUTH
}

destroy(){
	chkid $1
	DROPLET_ID=$1
	curl -s $URL'/droplets/'$DROPLET_ID'/destroy/?'$AUTH
}

create(){
	chkid $1
	DROPLET_NAME=$1
	SIZE_ID=62
	IMAGE_ID=$HNIMG
	REGION_ID=1
	SSH_KEY_ID1=8643
	curl -s $URL'/droplets/new?name='$DROPLET_NAME'&size_id='$SIZE_ID'&image_id='$IMAGE_ID'&region_id='$REGION_ID'&'$AUTH'&ssh_key_ids='$SSH_KEY_ID1
}

confirm_up(){
	status=`getdrops | grep -c '"status":"active"'`
	if [[ $status == "1" ]]; then
		echo "droplet is online"
	else
		echo "droplet is offline"
	fi
}

chkid(){
if [[ -z $1 ]]; then
	echo "an ID or NAME is required, see usage"
	exit 1
fi
}

case "$1" in
	getdrops|getimages|getkeys|showkey|dropstatus|startdrop|stopdrop|killdrop|create|destroy )
	$1 "$2"
	;;
	confirm )
	confirm_up
	;;
	* )
	echo $"Usage: $0 {getdrops|getimages [all]|getkeys|showkey|dropstatus|startdrop|stopdrop|killdrop|destroy|create} DROPLET_ID"
	echo "a valid DROPLET_ID is required for any action affecting a specific host"
	exit 1
esac
