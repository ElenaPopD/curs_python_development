FROM python:3.12
#instalex dependinte
RUN pip install flask
#adaug cod
ADD web.py .
ENTRYPOINT [ "python", "web.py" ]
EXPOSE 5000