VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :knossos do |knossos_config|

    knossos_config.vm.box = "precise64_base"
    knossos_config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    
    knossos_config.vm.network :private_network, ip: "192.168.100.100"
    
    knossos_config.vm.provider :virtualbox do |vb|
    
      vb.gui = true 
 
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["modifyvm", :id, "--graphicscontroller", "vboxvga"]
      vb.customize ["modifyvm", :id, "--accelerate3d", "on"]
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ["modifyvm", :id, "--vram", "128"]
      vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
    end

    knossos_config.ssh.forward_x11 = 'true'

    ## Frontend currently uses fabric to provision

  end

end
