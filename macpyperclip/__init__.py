import os
import platform
import subprocess

if platform.system() != 'Darwin':
    raise ImportError("This module is applicable only to Mac!")

__all__ = ['copy', 'paste']


def init_osx_clipboard():
    def copy_osx(text):
        p = subprocess.Popen(['pbcopy', 'w'], stdin=subprocess.PIPE, close_fds=True)
        p.communicate(input=text.encode('utf-8'))

    def paste_osx():
        p = subprocess.Popen(['pbpaste', 'r'], stdout=subprocess.PIPE, close_fds=True)
        stdout, stderr = p.communicate()
        return stdout.decode('utf-8')

    return copy_osx, paste_osx


copy, paste = init_osx_clipboard()
