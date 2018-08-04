import hashlib
import os
import sys

def which_python():
    if (sys.version_info > (3, 0)):
        return 3
    else:
        return 2

python_version = which_python()

def computeMD5hash(stringg):
    m = hashlib.md5()
    if python_version == 2:
        m.update(stringg.encode('utf8'))
    else:
        m.update(stringg)
    return m.hexdigest()

if not os.path.exists("md5/"):
    os.makedirs("md5/")

for root,dirs,files in os.walk('testcases/'):
    for file in files:
        if '.txt' in file:
            with open('testcases/'+file) as f:
                md5_string = computeMD5hash(f.read())
                f1 = open("md5/"+file, 'w')
                f1.write(md5_string)
                f1.close()