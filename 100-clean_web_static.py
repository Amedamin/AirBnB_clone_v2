#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["100.25.16.27", "54.237.109.157"]


def do_clean(number=0):
    """Deletes"""
