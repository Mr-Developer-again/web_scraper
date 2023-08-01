FROM python:3.9.7-slim
RUN apt update && mkdir /shared_files 
RUN pip3 install selenium
WORKDIR /app
COPY link_generator.py .
ENTRYPOINT ["python3", "link_generator.py"]