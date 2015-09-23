#!bin/bash
#Flask installation 

#Let's check for a virtualenv utility

if command -v virtualenv 2>&1
then 
	echo "Virtualenv is installed"
else 
	sudo apt-get install python-virtualenv
fi 

test -d $HOME/Flask || mkdir $HOME/Flask # Creating a directory
echo "Do you want to install examples? (y/n)"
read answ

case "$answ" in 
	"y" ) git clone https://github.com/miguelgrinberg/flasky.git;
		cd flasky; 
		git checkout 1a;;
	* ) ;;
esac

#creating virtual environment 
virtualenv venv
#activating ir
source venv/bin/activate
pip install flask 