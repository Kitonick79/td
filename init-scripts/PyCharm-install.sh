#bin/bash
#Installing PyCharm on a computer without jre
#After the installation check "Start from command line in pop up"
#To start form command line use charm

if command -v java 2>&1
then 
	echo "JRE is installed"
else 
	sudo apt-get install default-jre
fi 

cd 
test -d $HOME/PyCharm || mkdir $HOME/PyCharm #Creating a new directory
test -f $HOME/Downloads/pycharm-community-*.tar.gz || { echo "No distributive in Downloads"; exit 1; } #Checking if distributive exists
cp $HOME/Downloads/pycharm-community-*.tar.gz $HOME/PyCharm #Copy distibutive
tar -xf $HOME/PyCharm/pycharm-community-*.tar.gz #Unpack
rm $HOME/PyCharm/pycharm-community-*.tar.gz   #Removing distr
rm $HOME/Downloads/pycharm-community-*.tar.gz #Removing distr
exec PyCharm/pycharm-community-*/bin/pycharm.sh #Launching for the first time
