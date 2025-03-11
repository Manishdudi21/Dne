FROM python:3.12.1
WORKDIR /app
COPY . .
COPY Tools/mp4decrypt /usr/local/bin/mp4decrypt
RUN chmod +x /usr/local/bin/mp4decrypt
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    wget \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r master.txt

CMD ["python", "./main.py"]
