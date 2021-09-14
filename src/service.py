import random
import numpy as np
import json
from rdkit import Chem
from rdkit.Avalon import pyAvalonTools
from rdkit import DataStructs
from typing import List

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.common import JSONArtifact
from bentoml.types import JsonSerializable


NBITS = 1024
DTYPE = np.int8


class Descriptor(object):

    def __init__(self):
        self.nbits = NBITS

    def calc(self, mol):
        fp = pyAvalonTools.GetAvalonFP(mol, nBits=self.nbits)
        fp_np = np.zeros((1, self.nbits), dtype=DTYPE)
        DataStructs.ConvertToNumpyArray(fp, fp_np)
        return fp_np



@artifacts([JSONArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput(), batch=True)
    def calculate(self, input: List[JsonSerializable]):
        desc = Descriptor()
        input = input[0]
        output = []
        for inp in input:
            mol = Chem.MolFromSmiles(inp["input"])
            fp = desc.calc(mol)
            output += [{"fp": fp}]
        return [output]
