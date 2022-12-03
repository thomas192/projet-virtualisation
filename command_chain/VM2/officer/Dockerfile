FROM python:3.9-alpine
ADD . /code
WORKDIR /code
RUN apk update
RUN apk add libc6-compat
RUN chmod u+x spawn
CMD ["python", "-u", "execute.py"]
