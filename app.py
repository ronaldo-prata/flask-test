from functions import *
from flask import Flask, render_template, redirect, request, url_for

app=Flask(__name__)

@app.route("/")
def home():
	return redirect(url_for("drawMol", smiles = ""))

@app.route("/drawMolecule", methods = ['POST', 'GET'])
@app.route("/drawMolecule/", methods = ['POST', 'GET'])
@app.route("/drawMolecule/<smiles>", methods = ['POST', 'GET'])
def drawMol(smiles = ""):
	#If a SMILES has been submitted through the form.
	if (request.method == 'POST'):
		smiles = request.form['SMILES']
	im = ImageFromSmiles(smiles)
	#If the smiles is incorrect or is blank.
	if (not im or smiles == ""):
		#Draw the page without any images.
		return render_template('drawMolecule.html', title="SMILES Input")
	return render_template('drawMolecule.html', title=smiles, img=Imageto64(im))