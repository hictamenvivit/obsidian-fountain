FROM nikolaik/python-nodejs:latest

RUN npm install afterwriting -g
COPY main.py .
RUN pip install flask

CMD python main.py
