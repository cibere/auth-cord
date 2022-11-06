"""
auth-cord
~~~~~~~~~~~~~~~~~~~
A basic wrapper discord oauth2
"""

__description__ = "A basic wrapper discord oauth2"
__version__ = "0.1.2"

from .authorization import Authorization
from .client import Client

__FULL_VERSION__ = __version__
if __FULL_VERSION__.startswith("BETA"):
    try:
        import subprocess

        p = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = p.communicate()
        if out:
            __FULL_VERSION__ += out.decode("utf-8").strip()
        p = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = p.communicate()
        if out:
            __FULL_VERSION__ += "+g" + out.decode("utf-8").strip()
    except Exception:
        pass
