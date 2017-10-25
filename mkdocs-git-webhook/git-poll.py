import os
import subprocess
from argparse import ArgumentParser
from time import sleep

cb = __import__('mkdocs-callback')


def git_pull(git_repo_path):
    os.chdir(git_repo_path)

    try:
        subprocess.check_output(["git", "checkout", "master"])
        subprocess.check_output(["git", "pull", "origin", "master"])

    except subprocess.CalledProcessError as e:
        print "ERROR: there was a problem updating the repository: " + e.message
        exit(1)


def git_poll(git_repo_path, htdocs_path, interval):
    while True:
        sleep(interval)
        git_pull(git_repo_path)
        cb.run(git_repo_path, htdocs_path)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument('git_repo_path')
    p.add_argument('htdocs_path')
    p.add_argument("--interval", required=False, default=30) # polling interval, in seconds

    args = p.parse_args()

    git_poll(args.git_repo_path, args.htdocs_path, args.interval)
