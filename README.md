### knossos-vagrant

Rich Stoner, 11/18/2013

A quick attempt at getting knossos on my mac (10.8) without having to break anything in the process. 

Final goal: installed knossos in a VM, accessing data via shared folder (/vagrant/data), connected to through RDP (xrdp running on vm).

This requires VirtualBox 4.3+ with extension pack and Vagrant 1.3.5+.

#### Install instructions

Based on [https://code.google.com/p/knossos-skeletonizer/wiki/CompilingKnossosOnLinux](https://code.google.com/p/knossos-skeletonizer/wiki/CompilingKnossosOnLinux)

**Start vm**

	vagrant up
	
**config via fabric**

	fab vagrant sysinfo
	
	fab vagrant base
	

**ssh in and do more things**

	vagrant ssh
	
	sudo apt-get install build-essential
	

**get agar (still ssh'd in)**

	cd /vagrant
	
	wget http://stable.hypertriton.com/agar/agar-1.4.0.tar.gz
	
	tar xvzf agar-1.4.0.tar.gz
	
	cd agar-1.4.0
	
	export CC=gcc-4.4;
	
	./configure
	
	make
	
	sudo make install
	

**install sdlclipboard (still ssh'd in)**

	cd /vagrant

	hg clone http://hg.assembla.com/SDL_Clipboard
	 
	cd SDL_Clipboard/
	 
	ccmake .

*type 'c', 'c', 'g'*

	make
	
	sudo cp build/libSDL_Clipboard.so /usr/local/lib/
	
	sudo cp include/SDL_Clipboard.h /usr/include/SDL/
	 
**compile and install libcurl from source (still ssh'd in)**

from: [http://askubuntu.com/questions/173085/how-do-i-build-libcurl-from-source](http://askubuntu.com/questions/173085/how-do-i-build-libcurl-from-source)

	sudo apt-get build-dep curl
	
	wget https://github.com/bagder/curl/archive/master.zip
	
	unzip master.zip

	cd curl-master
	
	./buildconf
	
	./configure

	make
	
	sudo make install
	 

**grab knossos from svn and compile**

	cd /vagrant
	
	svn checkout http://knossos-skeletonizer.googlecode.com/svn/trunk/ knossos-skeletonizer-read-only
	
	cd knossos-skeletonizer-read-only
	
	make clean
	
	make
	


**install a display**

from [http://networkstatic.net/xrdp-an-easy-remote-desktop-setup-for-your-ubuntu-servers/](http://networkstatic.net/xrdp-an-easy-remote-desktop-setup-for-your-ubuntu-servers/)

	sudo apt-get install ubuntu-desktop --no-install-recommends

	sudo apt-get install xrdp

	/etc/init.d/xrdp start





	
	