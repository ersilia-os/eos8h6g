# Avalon fingerprint

Avalon is a path-based substructure key fingerprint (1024 bits), developed for substructure screen-out when searching. It is part of the Avalon Chemoinformatics Toolkit and has also been implemented as an external RDKit tool.

This model was incorporated on 2021-09-14.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8h6g`
- **Slug:** `avalon`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Fingerprint`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1024`
- **Output Consistency:** `Fixed`
- **Interpretation:** Bitvector representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feature_0000 | integer |  | Feature 0 of the Avalon fingerprints |
| feature_0001 | integer |  | Feature 1 of the Avalon fingerprints |
| feature_0002 | integer |  | Feature 2 of the Avalon fingerprints |
| feature_0003 | integer |  | Feature 3 of the Avalon fingerprints |
| feature_0004 | integer |  | Feature 4 of the Avalon fingerprints |
| feature_0005 | integer |  | Feature 5 of the Avalon fingerprints |
| feature_0006 | integer |  | Feature 6 of the Avalon fingerprints |
| feature_0007 | integer |  | Feature 7 of the Avalon fingerprints |
| feature_0008 | integer |  | Feature 8 of the Avalon fingerprints |
| feature_0009 | integer |  | Feature 9 of the Avalon fingerprints |

_10 of 1024 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8h6g](https://hub.docker.com/r/ersiliaos/eos8h6g)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8h6g.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8h6g.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `501`


### References
- **Source Code**: [https://github.com/rdkit/rdkit/tree/master/External/AvalonTools](https://github.com/rdkit/rdkit/tree/master/External/AvalonTools)
- **Publication**: [https://pubs.acs.org/doi/full/10.1021/ci050413p](https://pubs.acs.org/doi/full/10.1021/ci050413p)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2006`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8h6g
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8h6g
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
