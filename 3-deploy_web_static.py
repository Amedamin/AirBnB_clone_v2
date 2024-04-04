#!/usr/bin/python3
"""Fabric script"""

from fabric.api import *
import os
from datetime import datetime
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


def do_pack():
    """Function do pack"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    N = datetime.now()
    FN = (
        f"versions/web_static_{N.strftime('%Y%m%d_%H%M%S')}"
        + ".tgz"
    )
    local(f"tar -cvzf {FN} web_static")

    if os.path.exists(FN):
        return FN
    else:
        return None


def deploy():
    """Deploys the web_static"""
    A = do_pack()
    if A is None:
        return False
    return do_deploy(A)
