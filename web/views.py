from flask import Blueprint, render_template, request, jsonify, send_from_directory
from web.scan import run_sqlmap, run_nuclei, run_katana, run_dirsearch
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get('url')
    tool = data.get('tool')
    
    if tool == 'sqlmap':
        result_file = run_sqlmap(url)
    elif tool == 'nuclei':
        result_file = run_nuclei(url)
    elif tool == 'katana':
        result_file = run_katana(url)
    elif tool == 'dirsearch':
        result_file = run_dirsearch(url)
    else:
        result_file = None
    
    if result_file:
        return jsonify({'message': f'Results saved to {result_file}'})
    else:
        return jsonify({'message': 'Unknown tool'})

@main.route('/download/taget_scan')
def download_file(filename):
    return send_from_directory(os.getcwd(), filename, as_attachment=True)