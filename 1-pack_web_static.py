<<<<<<< HEAD
#!/usr/bin/python3

from fabric.api import env, run, local,hosts
from fabric.operations import put
from datetime import datetime
from os

env.hosts = ['<IP web-01', '<IP web-02>']
env.user = '<your-username>'
env.key_filename = '<path-to-ssh-key>'

=======
from fabric.api import env, run, local, hosts
from fabric.operations import put
from datetime import datetime
import os


env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<your-username>'
env.key_filename = '<path-to-ssh-key>'


>>>>>>> 745f6862305549cc531994299d0533657cb1008f
def do_clean(number=0):
    number = int(number)
    if number < 0:
        number = 0
    elif number == 1:
        number = 2
<<<<<<< HEAD
# Get a list of archives in the versions folder
=======

    # Get a list of archives in the versions folder
>>>>>>> 745f6862305549cc531994299d0533657cb1008f
    local_archives = local('ls -1t versions', capture=True).split('\n')
    archives_to_delete = local_archives[number:]

    # Delete unnecessary archives in the versions folder
    for archive in archives_to_delete:
        local('rm -f versions/{}'.format(archive))

    # Get a list of archives in the releases folder on the web servers
    remote_archives = run('ls -1t /data/web_static/releases').split('\n')
    archives_to_delete = remote_archives[number:]

    # Delete unnecessary archives in the releases folder on the web servers
    for archive in archives_to_delete:
        run('rm -f /data/web_static/releases/{}'.format(archive))
