import re;
import os;
import sys;

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage> python3 make_m3u.py <filelist>");
        exit();
    ifile = open(
