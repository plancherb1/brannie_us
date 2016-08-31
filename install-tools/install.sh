#!/bin/bash

# basic installs
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
sudo apt-get install python-pip
sudo apt-get install apache2
sudo apt-get install apache2-dev
sudo apt-get install python2.7-dev
sudo apt-get install libapache2-mod-wsgi
sudo pip install MySQL-python

# Uninstall old django by typing in
# python -c "import django; print(django.__path__)"
# Then cd to that directory and delete the django folder

# Install django 1.9.7 (known to be stable)
sudo pip install -U django==1.9.7
# Alternatively drop the -u and the ==1.9.7 and try the latest

# Download the website
cd ~
git clone https://github.com/plancherb1/brannie_us.git

# make it available to apache by overwriting the apache sites-
# available file to include our site
sudo cp ~/brannie_us/install-tools/000-default.conf /etc/apache2/sites-available/000-default.conf
sudo service apache2 stop
sudo service apache2 start
