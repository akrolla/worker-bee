import os
import threading
import subprocess

def func_that_does_work():
    subprocess.call(args=["gnome-terminal", "--command= python <insert whatever here>"])
    pass

def more_work():
    subprocess.call(args=["gnome-terminal", "--command= python3 <insert whatever here>"])
    pass


def more_work_work():
    subprocess.call(args=["gnome-terminal", "--command= python <insert whatever here>"])
    pass
