FROM ubuntu:latest

WORKDIR /spin-app

COPY . .

RUN apt-get update && apt-get install -y curl build-essential libssl-dev pkg-config \
    && chmod +x ./docker/install.sh && ./docker/install.sh \
    && mv ./spin ./docker

ADD ./docker/start.sh /
RUN chmod +x ./docker/start.sh

EXPOSE 3000

CMD ["./docker/start.sh"]