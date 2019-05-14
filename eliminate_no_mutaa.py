import sys
import re
import pandas as pd
import numpy as np

#usage: python eliminate_no_mutaa.py protein_id_excel output_file

#obtains mutated peptides from protein description, returns all possible locations of mutated aa in peptide 
def get_peptides(hit):
    peptides = []
    poss_comb = []
    no_hits = hit.split(';')
    for i in range(0, len(no_hits)):
       if no_hits[i].startswith('GN'):
          peptide = no_hits[i].split('|')
          if(len(peptide[3]) == 7):
             peptides.append(peptide[3])
    for pep in range(0,len(peptides)):
       beg = peptides[pep][0:4]
       end = peptides[pep][3:7]
       mid_1 = peptides[pep][1:5]
       mid_2 = peptides[pep][2:6]
       poss_comb = [beg, end, mid_1, mid_2]
    return poss_comb

def main():
   #file names passed as arguments
   excel_file = sys.argv[1]
   out_file = sys.argv[2]

   #open and read protein hits excel file; output dataframe
   pd_out = pd.read_excel(excel_file)
   out_df = pd.DataFrame()

   #gets columns sequence and protein description to determine whether mutation is present or not
   sequences = pd_out['Sequence']
   hits = pd_out['Protein Descriptions']
   line_no = 1
   for i in range(0, len(pd_out.index)):
      line_no += 1
      if hits[i].startswith('GN'):
         peptides = get_peptides(hits[i])
         if any(x in sequences[i] for x in peptides):
            out_df = out_df.append(pd_out.iloc[[i]])
      else:
         out_df = out_df.append(pd_out.iloc[[i]])

   out_df.to_excel(out_file)

main()
