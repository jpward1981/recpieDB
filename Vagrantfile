# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "box-cutter/fedora22"
  config.vm.box_check_update = true
#  config.vm.network "public_network", bridge: "en1: Wi-Fi (AirPort)"
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
  end
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yaml"
  end
end
