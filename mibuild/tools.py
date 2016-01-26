import os
import struct
from distutils.version import StrictVersion


def mkdir_noerror(d):
    try:
        os.mkdir(d)
    except OSError:
        pass


def language_by_filename(name):
    extension = name.rsplit(".")[-1]
    if extension in ["v", "vh", "vo"]:
        return "verilog"
    if extension in ["vhd", "vhdl", "vho"]:
        return "vhdl"
    return None


def write_to_file(filename, contents, force_unix=False):
    newline = None
    if force_unix:
        newline = "\n"
    if os.path.exists(filename):
        if open(filename, "r").read() == contents:
            return
    with open(filename, "w", newline=newline) as f:
        f.write(contents)


def arch_bits():
    return struct.calcsize("P")*8


def versions(path):
    for n in os.listdir(path):
        full = os.path.join(path, n)
        if not os.path.isdir(full):
            continue
        try:
            yield StrictVersion(n)
        except ValueError:
            continue
