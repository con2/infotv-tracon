FROM node:18
WORKDIR /usr/src/app
RUN git clone https://github.com/kcsry/infotv --depth=1 -b v0.4.1 && \
    rm -rf infotv/.git && \
    cd infotv/infotv/frontend && \
    npm install --legacy-peer-deps && \
    NODE_OPTIONS=--openssl-legacy-provider INFOTV_STYLE=tracon NODE_ENV=production npm run release && \
    rm -rf node_modules

FROM python:3.11
COPY --from=0 /usr/src/app/infotv /usr/src/app/infotv
RUN mkdir /usr/src/app/infotv-tracon && \
    groupadd -r infotv && useradd -r -g infotv infotv
WORKDIR /usr/src/app/infotv-tracon
COPY requirements.txt /usr/src/app/infotv-tracon/
RUN pip install --no-cache-dir -r requirements.txt -e ../infotv
COPY . /usr/src/app/infotv-tracon
RUN env DEBUG=1 python manage.py collectstatic --noinput && \
    python -m compileall -q .
USER infotv
EXPOSE 8000
ENTRYPOINT ["scripts/docker-entrypoint.sh"]
CMD ["gunicorn", "--bind=0.0.0.0", "--access-logfile=-", "--capture-output", "infotv_tracon.wsgi"]
