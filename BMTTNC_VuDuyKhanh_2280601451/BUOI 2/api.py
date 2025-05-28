from flask import Flask, request,jsonify
from cipher .caesar import CaesarCipher
app = Flask( __name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/decrypt",methods = ['POST']) 
