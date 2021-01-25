#!/opt/anaconda3/envs/cluster/bin/python
import sys

'''
This program is used to find orthologs for 2 or 3 species from a .blastp file using the Reciprocal Blast method.
Usage: 
    Input file: should be a .blastp file, 
        which is got by blasting a concatenated proteins from 2/3 species (e.g. ecat protein_sp1, protein_sp2 > concatenated.fas) blastped (e.g. blastp ....) against 
        the protein database built (e.g. makeblastdb -in concatenated.fas -out ** -dbtype prot) from the same concatenated protein file ()
    -num_description is suggested to set a large number in blastp, e.g. 50

    To find orthologs for 2 species, run the program: python OrthologFinder.py 2 outfile
    To find orthologs for 3 species, run the program: python OrthologFinder.py 3 sp1 sp2 sp3 outfile
        Here, sp1, sp2 and sp3 are the prefix that was added to the protein sequences (e.g. in the protein_sp1 file) to represent different species,
        e.g. Festuca ovina can have a prefix of Feso, at least the first 3 letters of sp1, sp2 and sp3 should be different from each other.  
'''

def parser(infile):    
    pre = []  #Seems we need to increase the output hits nr
    with open (infile, "r") as fin:
        for line in fin:  
            line=line.rstrip()
            if ("Query=" in line):
                Query = line.split()[1]
                t=0
            if "*****" in line:
                    t=1
                    target = " "
                    pre.append([Query, target])
            #Make sure the protein from different species:
            elif (line.startswith(">")) and (t == 0) and Query[0:3]!=line.split()[0][1:4]:
                    target = line.split()[0][1:]
                    t=2
                    pre.append([Query, target])
            elif ("Query=" in line) and t==0: 
                    target = " "
                    pre.append([Query, target])
    return(pre)


# Find orthogs from 2 different species
def findOrthPair(pre):
    orth = []
        for p in pre:
            if [p[1], p[0]] in pre:
                if ([p[0], p[1]] not in orth) and ([p[1], p[0]] not in orth):
                    orth.append([p[0], p[1]])
    return(orth)


#Sort the pair and write to file
def orthoPair(outfile):
    with open (outfile, "w") as outf:
        print("Species1", "Species2", sep="\t", file=outf)
        for o in orth:
            if o[0][0:3]==sp1[0:3]:
                print(o[0], o[1], file=outf) # sort them based on species when writing to file
            elif o[0][0:3]==sp2[0:3]:
                print(o[1], o[0], sep="\t", file=outf)


# Look for rtholog-triplets (from 3 organisms)
#build a dictrionary, where sp1 is the key, its ortholog is the value
def orthoPair_internal(sp1): 
    orthPair = {}
        for o in orth:
            if o[0][0:3]==sp1[0:3]:
                orthPair[o[0]] = o[1]
            elif o[1][0:3]==sp1[0:3]:
                orthPair[o[1]] = o[0]
    return(orthPair)
    

#collect all ortholog pairs that contain sp1, and order the pair so that sp1 comes first in the pair
def getOrthoTrip1(sp1_o, sp2_o, sp3_o)
    ortho_tri_1 = []
    for s1, s2 in sp1_o.items():
        if (s2 in sp2_o) and (sp2_o[s2][0:3] != s1[0:3]):
            ortho_tri_1.append((s1, s2, sp2_[o]))
        elif (s2 in sp3_o) and (sp3_o[s2][0:3] != s1[0:3]):
            ortho_tri_1.append((s1, sp3_o[s2], s2))
    return (ortho_tri_1)


#collect all ortholog pairs that contain sp2, and order the pair so that sp1 comes first in the pair
def getOrthoTrip2(sp1_o, sp2_o, sp3_o)
    ortho_tri_2 = []
    for s1, s2 in sp2_o.items():
        if (s2 in sp1_o) and (sp1_o[s2][0:3] != s1[0:3]):
            ortho_tri_2.append((s2, s1, sp1_[o]))
        elif (s2 in sp3_o) and (sp3_o[s2][0:3] != s1[0:3]):
            ortho_tri_2.append((sp3_o[s2], s1, s2))
    return(ortho_tri_2)

#collect all ortholog pairs that contain sp3, and order the pair so that sp1 comes first in the pair
def getOrthoTrip3(sp1_o, sp2_o, sp3_o)
    ortho_tri_3 = []
    for s1, s2 in sp3_o.items():
        if (s2 in sp1_o) and (sp1_o[s2][0:3] != s1[0:3]):
            ortho_tri_3.append((s2, sp2_[o]), s1)
        elif (s2 in sp2_o) and (sp2_o[s2][0:3] != s1[0:3]):
            ortho_tri_3.append((sp2_[o], s2, s1))
    return(ortho_tri_3)


#Write the triplets to a file
def orthoTriplet(outfile, sp1, sp2, sp3):
    with open (outfile, "w") as outfile:
        print(sp1, sp2, sp3, sep="\t")
        for tri in ortho_tri:
            print(tri[0], tri[1], tri[2], sep="\t")


if __name__ == "__main__":
    if sys.arg(2) = 2: #Find orthologs for two organisms
        pre = parser(sys.arg[1])
        ortho.pair = findOrthPair(pre)
        orthoPair(sys.arg[3])

    if sys.arg(2) = 3: #Find orthologs for 3 organism
        pre = parser(sys.arg[1])

        sp1_o = orthoPair_internal(sys.arg[3]) 
        sp2_o = orthoPair_internal(sys.arg[4]) 
        sp3_o = orthoPair_internal(sys.arg[5]) 

        ortho_tri_1 = getOrthoTrip1(sp1_o, sp2_o, sp3_o)
        ortho_tri_2 = getOrthoTrip2(sp1_o, sp2_o, sp3_o)
        ortho_tri_3 = getOrthoTrip3(sp1_o, sp2_o, sp3_o)

        ortho_tri = set(ortho_tri_1 + ortho_tri_2 + ortho_tri_3) # remove duplicates
        orthoTriplet(sys.arg[6], sp1, sp2, sp3)











