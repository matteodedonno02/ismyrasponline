## IS MY RASPBERRY ONLINE?
### Setup
- Replace TOKEN and CHAT_ID
- Copy python file to /bin
	```console
	sudo cp -i /path/to/ismyrasponlilne.py
	```
- Add a new cron job
	```console
	sudo crontab -e
	```
	Scroll to the bottom and add the following line
	```console
	@reboot python /bin/ismyrasponlilne.py &
	```

