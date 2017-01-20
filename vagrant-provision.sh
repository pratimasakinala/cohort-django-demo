#!/bin/bash

#########
## Setup

# Ensure everything is up to date
echo "Updating the system..."
sudo apt-get -y update
sudo apt-get -y upgrade


# Build tools and pre-reqs
echo "Installing developer tools..."
sudo apt-get -y install git build-essential libjpeg-dev libtiff5-dev zlib1g-dev
# libfreetype6-dev ziblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

# bash history completion
wget https://raw.githubusercontent.com/dmpayton/dotfiles/master/.inputrc -O ~ubuntu/.inputrc
chown ubuntu:ubuntu ~ubuntu/.inputrc

##########
## Python

echo "Installing Python 3..."
sudo apt-get install -y python3 python3-dev

# pip
wget https://bootstrap.pypa.io/get-pip.py -O - | python3.5

# virtualenv
echo "Installing and configuring virtualenv and virtualenvwrapper..."

sudo pip install virtualenv virtualenvwrapper

mkdir ~ubuntu/.virtualenvs

printf "\n\n# Virtualenv settings\n" >> ~ubuntu/.bashrc
printf "export PYTHONPATH=/usr/lib/python3.5\n" >> ~ubuntu/.bashrc
printf "export WORKON_HOME=~ubuntu/.virtualenvs\n" >> ~ubuntu/.bashrc
printf "export PROJECT_HOME=/vagrant\n" >> ~ubuntu/.bashrc
printf "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.5\n" >> ~ubuntu/.bashrc
printf "source /usr/local/bin/virtualenvwrapper.sh\n" >> ~ubuntu/.bashrc
printf "workon venv\n" >> ~ubuntu/.bashrc

export PYTHONPATH=/usr/lib/python3.5
export WORKON_HOME=~ubuntu/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.5
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv venv

chown -R ubuntu:ubuntu ~ubuntu/.virtualenvs


########
## Node

echo "Installing Node.js..."
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs


##############
## PostgreSQL

echo "Installing PostgreSQL..."
apt-get install -y postgresql libpq-dev
# Create vagrant pgsql superuser
su - postgres -c "createuser --superuser vagrant"


#############
## Memcached

echo "Installing Memcached..."
apt-get install -y memcached libmemcached-dev


#########
## Done!

echo ""
echo "Vagrant setup complete!"
echo "Now try logging in:"
echo "    $ vagrant ssh"
