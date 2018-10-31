from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO
from PIL import ImageOps
import base64

#Trims the image into a box, removing any excess white background
def wTrim(img):
	bbox = ImageOps.invert(img).getbbox()
	if (bbox[2]-bbox[0] < 400 and bbox[3]-bbox[1] < 400):
		crop = (300, 300, 700, 700)
	elif (bbox[2]-bbox[0] > bbox[3]-bbox[1]):
		crop = (bbox[0], bbox[0], bbox[2], bbox[2])
	else:
		crop = (bbox[1], bbox[1], bbox[3], bbox[3])
	return img.crop(crop)
	
#Generates an image of the molecule represented by the SMILES code given.
#Returns None if the image cannot be generated.
def ImageFromSmiles(smiles):
	image = None
	if type(smiles) is str:
		try:
			image = Draw.MolToImage(Chem.MolFromSmiles(smiles), size=(1000, 1000))
		except ValueError:
			pass
	return image

#Converts a PIL image into its base64 representation.
def Imageto64(img):
	img = wTrim(img)
	buf = BytesIO()
	img.save(buf, format="PNG")
	return base64.b64encode(buf.getvalue()).decode("utf-8")
