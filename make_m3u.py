import re;
import os;
import sys;

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage> python3 make_m3u.py <filelist>");
        exit();
    ifile = open(sys.argv[1],"r");
    found = re.compile('trying to save (\w+://\d+.\d+.\d+.\d+:\d+) to');
    for line in ifile:
        match = found.search(line);
        print(match.group(1));
        
