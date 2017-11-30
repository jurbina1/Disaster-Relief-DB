from flask import Flask, jsonify

@app.route('/')
def home():
    return 'Disaster Relief'
