# XMAn_nonmutated_peptides
This script eliminates the hits reported from protein identification tools (proteomics) without the mutated amino acid in the sequence.

## **Input**

1. A file in EXCEL format (.xlsx) containing 2 columns with the exact following names: Sequence and Protein Descriptions. 
   - Sequence column contains the hit sequences reported by the protein identification tool.
   - Protein Descriptions contains the descriptions of the hits and these need to include the short sequence from the XMAn.v2 headers.

## **Usage**

*Linux/Mac*

git clone https://github.com/maguileraf/XMAn_nohit.git

cd XMAn_nohit

python eliminate_no_mutaa.py protein_id_excel_filename output_filename
