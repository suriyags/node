FROM python:3
COPY . /usr/src/app
CMD ["python", "api.py"]