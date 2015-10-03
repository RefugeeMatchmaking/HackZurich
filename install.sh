#!/bin/bash

# Installation virtual environment
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
sudo pip3 install virtualenvwrapper


# Echo virtualenvironment things into bashrc, also for python3 compatibility
echo "
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/vagrant
source /usr/local/bin/virtualenvwrapper.sh
" >> /home/vagrant/.bashrc

source /home/vagrant.bashrc

# Activate virtualenv and install django
mkvirtualenv refugee_matchmaking
pip3 install -r /vagrant/requirements.txt