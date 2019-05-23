# XMAn_nonmutated_peptides
This script eliminates the hits reported from protein identification tools (proteomics) without the mutated amino acid in the sequence.

## **Input**

1. A file in EXCEL format (.xlsx) containing any columns but 2 columns with the exact following names: Sequence and Protein Descriptions. 
   - Sequence column contains the hit sequences reported by the protein identification tool.
   - Protein Descriptions contains the descriptions of the hits and these need to include the short sequence from the XMAn.v2 headers. (e.g. GN=CDC42BPB MRCKB_HUMAN Serine/threonine-protein kinase MRCK beta|c_C3625A|p_L1209I|VGIIEGL|Missense)
   
## **Dependencies**

pandas

openpyxl

xlrd

## **Usage**


**Linux/Mac**

Install dependencies with pip:

$ `pip install pandas`

$ `pip install xlrd`

$ `pip install openpyxl`

$ `git clone https://github.com/lazarlab/XMAn-v2.git`

$ `cd XMAn-v2/`

$ `python eliminate_nonmut_peptides.py protein_id_excel_filename output_filename`

**Windows**

download python (https://www.python.org/downloads/)

Go to windows start and in search type 'cmd' and click to open

Type the following commands followed by enter to install dependencies:

$ `pip install pandas`

$ `pip install xlrd`

$ `pip install openpyxl`

download this repository as a zip folder under the green botton "Clone or download"

unzip the folder

Type the following commands followed by enter to run the script:

$ `cd PathToDownloadedRepository\XMan-v2-master` (if in Downloads type cd Downloads\XMan-v2-master\XMan-v2-master)

$ `python eliminate_nonmut_peptides.py <input_filename>.xlsx <output_filename>.xlsx`
