from flask import Flask, jsonify

@app.route('/')
def home():
    return 'Disaster Relief'

if __name__=='__main__':
    app.run()
