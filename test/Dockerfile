FROM python:3.12
#instalez dependinte
RUN pip3 install django
#adaug cod
ADD my_project .
WORKDIR my_project
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]