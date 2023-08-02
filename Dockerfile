FROM python:3.10-slim
WORKDIR /app
COPY ./ /app
RUN python -m pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir
EXPOSE 8020
STOPSIGNAL SIGTERM
ENTRYPOINT ["/app/start_server.sh"]