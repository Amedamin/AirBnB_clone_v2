#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ["100.25.16.27", "54.237.109.157"]

def do_deploy(archive_path):
    """
    Distributes an archive
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        F = os.path.basename(archive_path)
        N = os.path.splitext(AF)[0]
        P = f"/data/web_static/releases/{N}"
        run(f"mkdir -p {P}")
        run(f"tar -xzf /tmp/{F} -C {P}")
        run(f"rm /tmp/{F}")
        run(f"mv {P}/web_static/* {P}")
        run(f"rm -rf {P}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {P} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        return False
