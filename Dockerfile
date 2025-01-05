FROM python:latest

WORKDIR /data/

COPY ./mongofind.py/ .
COPY ./mongo-insertone.py/ .

RUN pip install requests
RUN pip install pymongo

#CMD ["ls"]
CMD ["/bin/bash"]