import os, sys, re, shutil

def get_Param_In_Command(nb_file):
    """
    Paramètre(s) entrée en ligne de commande inséré(s) dans une liste
    INPUT = nombre de parametre
    OUTPUT = Les option choisie
    """
    option = []
    for i in range(1, nb_file):
        if "-" not in sys.argv[i]:
            pass
        else:
            option.append(sys.argv[i])
    return option



if(len(sys.argv)>=2):
    # get file to split in command line
    option = get_Param_In_Command(len(sys.argv))

files=[]
if "-f" or "-F" in option:
    with open(sys.argv[len(option)+1]) as target:
        for line in target:
            files.append(line[:-1])
else:
    files.append(sys.argv[len(option)+1])

peaksign=[48, 16]
physicalSep=True
if physicalSep:
    try:
        shutil.rmtree("valley/")
        shutil.rmtree("peak/")
    except:
        pass
    os.makedirs("valley/")
    os.makedirs("peak/")
    for fileIn in files:
        with open(str(fileIn)) as file:
            peak=0
            valley=0
            for line in file:
                if re.search(r"^[0-9].*$", line):
                    elem=line.split("\t")[16]
                    if int(elem) in peaksign:
                        peak+=1
                    else:
                        valley+=1
        with open(fileIn) as file:
            fvalley=open("valley/"+str(fileIn), "w+")
            fpeak=open("peak/"+str(fileIn), "w+")
            for line in file:
                if re.search(r"^[0-9].*$", line):
                    elem=line.split("\t")[16]
                    if int(elem) in peaksign:
                        fpeak.write(line)
                        peak+=1
                    else:
                        fvalley.write(line)
                        valley+=1
                else:
                    if re.search(r"^Features:.*$", line):
                        fvalley.write("Features: "+str(valley) + "\n")
                        fpeak.write("Features: "+str(peak) + "\n")
                    else:
                        fvalley.write(line)
                        fpeak.write(line)
            fvalley.close()
            fpeak.close()
else:
    for file in files:
        print(file)
        fstem=open(file, "r")
        foutput=open("TO_SPLIT/" +file, "w+")
        for line in fstem:
            if re.search(r"^[0-9].*$", line):
                elem=line.split("\t")
                if not int(elem[16]) in peaksign:
                    for i in range(64):
                        elem[17+i] = (int(elem[17+i])+1)*-1
                for i in range(len(elem)):
                    if i<len(elem)-1:
                        foutput.write(str(elem[i]) + '\t')
                    else:
                        foutput.write(str(elem[i]))
            else:
                foutput.write(line)
        foutput.close()
