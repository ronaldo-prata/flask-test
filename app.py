from functions import *
import base64
from io import BytesIO
from flask import Flask, make_response, render_template

app=Flask(__name__)

@app.route("/")
def home():
	return "Please access the route /drawMolecule/"

@app.route("/drawMolecule/")
@app.route("/drawMolecule")
def info():
	res = make_response("Please enter SMILES code after url\n\nExample: /drawMolecule/CC(=O)Nc1ccc(O)cc1")
	res.headers["content-type"] = "text/plain"
	return res

@app.route("/drawMolecule/<smiles>")
def drawMol(smiles):
	im = ImageFromSmiles(smiles)
	if (not im):
		return "Invalid SMILES"
	buf = BytesIO()
	im.save(buf, format="PNG")
	img64 = base64.b64encode(buf.getvalue()).decode("utf-8")
	return render_template('drawMolecule.html', smiles = smiles, img=img64)