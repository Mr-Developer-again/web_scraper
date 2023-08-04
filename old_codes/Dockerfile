FROM python:3.9.7-slim
RUN apt update && mkdir /shared_files 
COPY link_generator.py requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["python3", "link_generator.py"]