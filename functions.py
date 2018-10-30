from rdkit import Chem
from rdkit.Chem import Draw

def ImageFromSmiles(smiles):
	image = None
	if type(smiles) is str:
		try:
			image = Draw.MolToImage(Chem.MolFromSmiles(smiles))
		except ValueError:
			return
	return image