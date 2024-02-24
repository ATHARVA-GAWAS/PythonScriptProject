from flask import render_template, request, redirect
import os
from extract_data import main

from app import app

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        # Call the data extraction script
        csv_file_path = 'output.csv'
        main(file_path, csv_file_path)
        # Read the CSV file
        data = []
        with open(csv_file_path, 'r') as csv_file:
            data = csv_file.readlines()
        # Pass the data to the result template
        return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
