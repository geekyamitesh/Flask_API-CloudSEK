FROM python:alpine3.8
COPY . /app
WORKDIR /app
RUN apk add build-base
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

