FROM onelouder/git-webhook:latest
COPY requirements.txt /requirements.txt
COPY mkdocs-callback.py /flask/app/mkdocs-callback.py
COPY git-poll.py /flask/app/git-poll.py
RUN pip install -r /requirements.txt
ENV CALLBACK mkdocs-callback