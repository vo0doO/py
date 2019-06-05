import os, sys
myf = []
myd = []
allf = []
alld = []
path = None
dirs = None
files = None
gp = "/home/vo0/WebstormProjects/kirsanov-do-personal-site/"
sys.path.insert(0, gp)

def get_full_path_to_file():
    for path, dirs, files in os.walk(gp):
      for f in files:
              allf.append(str(path) + "/"+ str(f))
    return allf
get_full_path_to_file()
for f in allf:
    print(str(f))
    if "elliott" in f:
        myf.append(f)


for f in myf:
    # renaming directory ''tutorialsdir"
    os.rename(f, f.replace('elliott', 'kirsanov'))
    print("Successfully renamed.")
    # listing directories after renaming "python3"
    #print("the dir is: %s" % os.listdir(os.getcwd()))
