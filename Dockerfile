FROM python:3.9-slim

COPY entrypoint.sh /entrypoint.sh
COPY compare_version.py /compare_version.py

RUN pip install toml gitpython

ENTRYPOINT ["/entrypoint.sh"]
