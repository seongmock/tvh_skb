import os;
for i in range(1,254):
	cmd = "sudo ../omvs -i 2 -u -j 5 239.192.%d.0/27 >> iplist.list"%i;
	print(cmd);
	os.system(cmd);
