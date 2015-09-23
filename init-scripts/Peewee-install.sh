#!bin/bash

virtualenv venv
if command -v peewee 2>&1
then 
	echo "peewee is installed"
else 
	#virtualenv venv
	sudo pip install peewee
fi 
