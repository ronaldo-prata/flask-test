# Flask Service for Molecular Drawing

This project is composed of a simple offline Flask service for drawing images of molecules described based on their SMILES representations.

## Installation

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
