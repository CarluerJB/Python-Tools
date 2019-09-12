import sys
from termcolor import colored

def unique(data):
  return list(dict.fromkeys(data))

def get_Param_In_Command(nb_file):
    """
    Paramètre(s) entrée en ligne de commande inséré(s) dans une liste
    INPUT = nombre de fichier à traiter <INT>
    OUTPUT = Les noms de fichiers en .fasta <LIST>
    """
    file = []
    option = []
    for i in range(1, nb_file):
        if "-" not in sys.argv[i]:
            file.append(sys.argv[i])
        else:
            option.append(sys.argv[i])
    return file, option

if(len(sys.argv)>=2):
    files, option = get_Param_In_Command(len(sys.argv))
    ListFile=[]
    verbose=False
    if "-v" in option:
        verbose=True
    for file in files:
        ListFile.append(open(file))
else:
    file1=open("match1.txt")
    file2=open("match2.txt")



for file in range(len(files)):
    temp=files[file].split('.')
    if len(temp)>5:
        temp=temp[1]

        files[file]=temp
        print(temp)
    else:
        files[file]=temp[0]


file1Index=len(ListFile)-1
x_y_z_scale1=[]
x_y_z_scale2=[]
for file2Index in range(len(ListFile)):
    commonmatch=0
    commonmatch2=0
    x_y_z_scale1=[]
    x_y_z_scale2=[]
    print("\n\n", colored(files[file1Index], attrs=['bold']), end='')
    print(colored(" to " + str(files[file2Index]), attrs=['bold']))

    if file2Index==file1Index:
        continue
    for line in ListFile[file1Index]:
        if '#' in line[0]:
            continue
        x_y_z_scale1.append(line.split('\t')[1:-2])
    for line in ListFile[file2Index]:
        if '#' in line[0]:
            continue
        x_y_z_scale2.append(line.split('\t')[1:-2])

    x_y_z_scale2=[x_y_z_scale2[i] for i in range(len(x_y_z_scale2)) if i == 0 or x_y_z_scale2[i] != x_y_z_scale2[i-1]]
    x_y_z_scale1=[x_y_z_scale1[i] for i in range(len(x_y_z_scale1)) if i == 0 or x_y_z_scale1[i] != x_y_z_scale1[i-1]]
    for pos in x_y_z_scale1:
        if pos in x_y_z_scale2:
            if verbose==True:
                print("\t",colored(pos, "green"))
            commonmatch+=1
        if not pos in x_y_z_scale2:
            if verbose==True:
                print("\t",colored(pos, "red"))
    for pos in x_y_z_scale2:
        if pos in x_y_z_scale1:
            commonmatch2+=1
    print("\0",colored(str(commonmatch)+"/"+str(len(x_y_z_scale1))+" matches found", attrs=['underline']))

    ListFile[file1Index].seek(0)
    ListFile[file2Index].seek(0)
    file1Index-=1
print("\n\n")
