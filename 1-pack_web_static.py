#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function do pack"""
    try:
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
    except Exception as e:
        return None
