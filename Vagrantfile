# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
config.vm.box = "ubuntu/trusty64"
config.vm.network "forwarded_port", guest: 8000, host: 8000
config.vm.synced_folder ".", "/home/vagrant/."
config.vm.provision :shell, path: "bootstrap.sh"
end
