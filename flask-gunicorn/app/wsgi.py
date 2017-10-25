import os
from app import app as application

if __name__ == "__main__":
    if 'APP_PORT' in os.environ.keys():
        application.run(port=os.environ["APP_PORT"])
    else:
        application.run()