import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def process_webhook():
    status_code = 500

    data = request.get_json()
    branches = map(lambda x: x['new']['name'], filter(lambda x: True if x['new']['type'] == 'branch' else False, data['push']['changes']))

    if 'master' not in branches:
        print "No changes to master branch in last push -- nothing to do!"

    else:
        if 'GIT_REPO_PATH' not in os.environ.keys():
            print "ERROR: no repo directory specified!"
            exit(1)

        os.chdir(os.environ['GIT_REPO_PATH'])

        try:
            subprocess.check_output(["git", "checkout", "master"])
            subprocess.check_output(["git", "pull", "origin", "master"])

        except subprocess.CalledProcessError as e:
            print "ERROR: there was a problem updating the repository: " + e.message
            exit(1)

        if 'CALLBACK' in os.environ.keys():
            cb = __import__(os.environ['CALLBACK'])
            cb.run(os.environ['GIT_REPO_PATH'])
            status_code = 200

    return jsonify("Success!"), status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0')
