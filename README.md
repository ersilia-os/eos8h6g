# Avalon Fingerprints

### Model Identifiers
* Slug: avalon
* Ersilia ID: eos8h6g
* Tags: fingerprint, ML, substructure

## Model Description
Substructure fingerprint for similarity search based on 16 features of the molecular graph
* Input: SMILES
* Output: 1024-bit vector (Bitvector representation of a molecule)
* Model type: Regression
* Training set: 143,000 compounds (link?)

## Source code
This model has been developed and published by:
Peter Gedeck, Bernhard Rohde, and Christian Bartels. QSAR − How Good Is It in Practice? Comparison of Descriptor Sets on an Unbiased Cross Section of Corporate Data Sets. *Journal of Chemical Information and Modeling* 2006 46 (5), 1924-1936 DOI: [10.1021/ci050413p](https://pubs.acs.org/doi/full/10.1021/ci050413p)

* Code: https://github.com/rdkit/rdkit/tree/master/External/AvalonTools
* Checkpoints: the model checkpoints were obtained from the source publication

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "Avalon Tools", located at `/src` and licensed under a [BSD-3 License](https://github.com/ersilia-os/eos8h6g/blob/main/src/LICENSE)

## History
- The model was downloaded and incorporated on September 13, 2021
