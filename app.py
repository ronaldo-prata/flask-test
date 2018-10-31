from functions import *
from flask import Flask, render_template, redirect, request, url_for

app=Flask(__name__)

@app.route("/")
def home():
	return redirect(url_for('info'))

@app.route("/drawMolecule/", methods = ['POST', 'GET'])
def info():
	if request.method == 'POST':
		htmlSmiles = request.form['SMILES'].replace("\\", "%5C").replace("/", "%2F")
		return redirect(url_for('drawMol', smiles=htmlSmiles))
	return render_template('drawMoleculeForm.html')

@app.route("/drawMolecule/<smiles>/")
def drawMol(smiles):
	smiles = smiles.replace("%5C", "\\").replace("%2F", "/")
	im = ImageFromSmiles(smiles)
	if (not im):
		return "Invalid SMILES"
	return render_template('drawMolecule.html', smiles = smiles, img=Imageto64(im))