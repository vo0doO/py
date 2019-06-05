import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from t import get_full_path_to_file
import fileinput



allf = get_full_path_to_file()
count = 0
while count <= len(allf):
    try:
        filename = allf[count]
        with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
            for line in file:
                line = line.rstrip()  # remove trailing (invisible) space
                print('kirsanov' if line == 'elliott' else line)  # stdout is redirected to the file
        os.unlink(filename + '.bak')
    except Exception as ERROR:
        print(ERROR.args)
    count +=1
# Elliott Marquez



#with open(, "r") as f:
#    txt = f.readlines()
#    print(txt)
#    for line in txt:
#        if "elliott" in line:
#            line.replace("elliott", "kirsanov")
#        if "Elliott" in line:
#            print(f"!!!!!!!! + {line} + !!!!!!!!!!")