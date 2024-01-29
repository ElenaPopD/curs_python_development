FROM python:3.12
#instalez dependinte
RUN apt-get update && apt-get install build-essential graphviz graphviz-dev --assume-yes
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#adaug cod
ADD my_project .
WORKDIR my_project
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
