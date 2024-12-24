import subprocess
import os

def run_sqlmap(url):
    command = f"sqlmap -u {url} --batch"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    result_file = os.path.join(os.getcwd(), 'sqlmap_result.txt')
    with open(result_file, 'w') as file:
        file.write(output.decode('utf-8'))
    return 'sqlmap_result.txt'

def run_nuclei(url):
    command = f"nuclei -u {url} -s critical,high,medium"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    result_file = os.path.join(os.getcwd(), 'nuclei_result.txt')
    with open(result_file, 'w') as file:
        file.write(output.decode('utf-8'))
    return 'nuclei_result.txt'

def run_katana(url):
    command = f"katana scan -u {url} -p xss,sql"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    result_file = os.path.join(os.getcwd(), 'katana_result.txt')
    with open(result_file, 'w') as file:
        file.write(output.decode('utf-8'))
    return 'katana_result.txt'

def run_dirsearch(url):
    command = f"dirsearch -u {url} -e sh,txt,htm,php,cgi,html,pl,bak,old"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    result_file = os.path.join(os.getcwd(), 'dirsearch_result.txt')
    with open(result_file, 'w') as file:
        file.write(output.decode('utf-8'))
    return 'dirsearch_result.txt'