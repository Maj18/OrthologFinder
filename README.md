# OrthologFinder

This program is used to find orthologs for 2 or 3 species from a .blastp file using the Reciprocal Blast method.

**Usage**: 

    *Input file: should be a .blastp file, 

        * which is got by blasting a concatenated proteins from 2/3 species (e.g. ecat protein_sp1, protein_sp2 > concatenated.fas) blastped (e.g. blastp ....) against 
        the protein database built (e.g. makeblastdb -in concatenated.fas -out ** -dbtype prot) from the same concatenated protein file ()

    *-num_description is suggested to set a large number in blastp, e.g. 50

    *To find orthologs for 2 species, run the program: python reciprocalBlast.py 2 outfile
    
    *To find orthologs for 3 species, run the program: python reciprocalblast.py 3 sp1 sp2 sp3 outfile
    
        * Here, sp1, sp2 and sp3 are the prefix that was added to the protein sequences (e.g. in the protein_sp1 file) to represent different species,
        e.g. Festuca ovina can have a prefix of Feso, at least the first 3 letters of sp1, sp2 and sp3 should be different from each other.  # OrthologFinder
