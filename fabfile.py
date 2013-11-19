from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import exists

from datetime import datetime
import sys, pprint, time, ConfigParser, os

def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['192.168.100.100']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config knossos | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
    


def sysinfo():
    run('uname -a')
    run('lsb_release -a')


def base():
    '''[create] Basic packages for building, version control'''
    
    with settings(warn_only=True):

        run("sudo apt-get -y update", pty = True)
        run("sudo apt-get -y upgrade", pty = True)


        packages = [
            'libsdl1.2-dev',
            'python-tk',
            'bison',
            'flex',
            'gcc-4.4',
            'cmake-curses-gui',
            'g++',
            'libxml2-dev',
            'libsdl-net1.2-dev',
            'freeglut3-dev',
            'libfreetype6-dev',
            'mercurial',
            'build-essential',
            'subversion',
            'git',
            'unzip'
        ]

        # packagelist = ' '.join(['git-core', 'mercurial', 'subversion', 'unzip', 'build-essential', 'g++','uuid-dev',
                                # 'redis-server', 'nginx'])

        packagelist = ' '.join(packages)

        run('sudo apt-get -y install %s' % packagelist, pty = True)

        # packagelist = ' '.join(['python-setuptools', 'python-pip', 'python-dev', 'python-lxml', 'libxml2-dev'])

        # #packagelist = ' '.join(['python-setuptools', 'python-pip', 'python-dev', 'python-lxml', 'libxml2-dev', 'python-imaging', 'libncurses5-dev', 'cmake-curses-gui', 'imagemagick'])
        # run('sudo apt-get -y install %s' % packagelist, pty = True)
        
        # packagelist = ['tornado', 'supervisor', 'virtualenv' ]
        # for each_package in packagelist: 
        #     print each_package
        #     run('sudo pip install %s' % each_package, pty = True)


