# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = true
  config.vm.network "public_network", bridge: "en1: Wi-Fi (AirPort)"
  config.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
  end
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yaml"
  end
end
