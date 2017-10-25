import os
import subprocess


def run(workdir, destination_dir):
    try:
        os.chdir(workdir)

    except OSError as e:
        print "ERROR: there was a problem rebuilding the documentation: " + e.message
        exit(1)

    try:
        subprocess.check_call(
            [
                'mkdocs',
                'build'
            ]
        )
        subprocess.check_call(
            [
                "ls",
                "-al"
            ]
        )
        subprocess.check_call(
            [
                'bash',
                '-c',
                'cp -R site/* {}'.format(destination_dir)
            ]
        )

    except subprocess.CalledProcessError as e:
        print "ERROR: there was a problem rebuilding the documentation: " + e.message
        exit(1)



