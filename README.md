# Flask Service for Molecular Drawing

This project is composed of a simple offline Flask service for drawing images of molecules described based on their SMILES representations.

## Installing

Running this project requires the *rdkit* library, available through *anaconda*:

```
conda install -c rdkit rdkit
```

Afterwards, it's necessary to create a virtual environment and install Flask in it:

```
conda create -n *env_name*
source activate *env_name*
pip install Flask
```

Finally, some environment variable must be set to run the Flask service:

```
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```

## Running

The site consists of a single route, /drawMolecule/, which can be used in two ways:

* Acessing the base route /drawMolecule/, a molecule's SMILE representation can be input and submited to generate it's corresponding image visualization.
* Alternatively, the SMILES code can be directly input on the URL after the route, such as /drawMolecule/\<SMILES\>, which should also generate a corresponding image but only in cases where the SMILES doesn't contain special characters that interfere with the html parsing, such as #, \ and /