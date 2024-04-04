#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = ['my_ssh_private_key']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        number = int(number)
    except ValueError:
        number = 1

    if number < 1:
        number = 1

    # Local path to the archives
    local_path = "./versions"

    with cd('/data/web_static/releases'):
        # Get list of archives
        archives = run("ls -t").split()

        # Keep only the most recent 'number' archives
        to_delete = archives[number:]

        for archive in to_delete:
            if archive.strip():
                run("rm -f {}".format(archive))

    with lcd(local_path):
        # Get list of local archives
        local_archives = local("ls -t", capture=True).split()

        # Keep only the most recent 'number' local archives
        to_delete_local = local_archives[number:]

        for local_archive in to_delete_local:
            if local_archive.strip():
                local("rm -f {}".format(local_archive))


if __name__ == "__main__":
    do_clean()
