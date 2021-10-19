FROM python:3.7.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5432 8050 6379 3128

CMD [ "python3", "./go_spider.py"]