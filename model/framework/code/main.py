# imports
import os
import csv
import sys
import numpy as np
from rdkit import Chem
from rdkit.Avalon import pyAvalonTools
from rdkit import DataStructs

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

NBITS = 1024
DTYPE = np.int8

def calc(mol):
    fp = pyAvalonTools.GetAvalonFP(mol, nBits=NBITS)
    fp_np = np.zeros((1, NBITS), dtype=DTYPE)
    DataStructs.ConvertToNumpyArray(fp, fp_np)
    return fp_np


def get_fp(smi_list):
    output = []
    for smi in smi_list:
        mol = Chem.MolFromSmiles(smi)
        fp = calc(mol)
        output += [fp]
    return output

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = get_fp(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow([f"feature_{i:04}" for i in range(1024)])  # header
    for o in outputs:
        writer.writerow(o)