from fabric.api import local
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

