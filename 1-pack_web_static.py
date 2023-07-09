#!/usr/bin/python3

from fabric.api import env, run, local,hosts
from fabric.operations import put
from datetime import datetime
import os

env.hosts = ['<IP web-01', '<IP web-02>']
env.user = '<your-username>'
env.key_filename = '<path-to-ssh-key>'

=======
from fabric.api import env, run, local, hosts
from fabric.operations import put
=======
from fabric.api import local
>>>>>>> b47fbe3830fded5ddb9e362c62ee79f156fb599d
from datetime import datetime
import os


def do_pack():
    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into the archive
    local("tar -czvf versions/{} web_static".format(archive_name))

    # Return the path to the archive if it has been successfully generated
    if os.path.exists("versions/{}".format(archive_name)):
        return "versions/{}".format(archive_name)
    else:
        return None

