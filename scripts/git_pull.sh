#!

cd /home/pi/git/speedtest
echo $HOSTNAME

if [ ''$HOSTNAME'' = ''LC99'' ]; then
	echo "we are updating"
	cd ~/git/speedtest
    echo $PWD
	git pull
	git fetch
	git checkout test5
    cd src 
    ./update_speedtest
	cd /home/pi
	
	
else
	git pull
	echo "updating dropbox"
	pip3 install --upgrade dropbox
	echo "updated dropbox"
    cd /home/pi
fi


