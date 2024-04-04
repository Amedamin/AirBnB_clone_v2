#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["100.25.16.27", "54.237.109.157"]


def do_clean(number=0):
    """Deletes"""
    with cd("/data/web_static/releases"):
        files = run("ls -1t").split("\n")
        n = int(number)
        if n in (0, 1):
            n = 1
        for i in files[n:]:
            if i != "test":
                run("rm -rf {}".format(i))
    
    with lcd("versions"):
        files = local("ls -1t", capture=True).split("\n")
        n = int(number)
        if n in (0, 1):
            n = 1
        for i in files[n:]:
            local("rm {}".format(i))
