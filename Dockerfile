FROM python:3

ENV API_ID=7127168592
ENV API_HASH=a90c6b05200b8df1c1bbbf63ca18a435

RUN apt update && apt upgrade -y; apt-get install git curl zip neofetch ffmpeg -y

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r req*

CMD ["bash", "start.sh"]
