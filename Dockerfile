FROM python:2.7
WORKDIR /usr/src/app
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get -y install nodejs
RUN git clone --depth=1 https://github.com/kcsry/infotv && \
    rm -rf infotv/.git && \
    cd infotv/infotv/frontend && \
    npm install && \
    INFOTV_STYLE=tracon NODE_ENV=production node_modules/.bin/gulp build && \
    rm -rf node_modules && \
    mkdir /usr/src/app/infotv-tracon && \
    groupadd -r infotv && useradd -r -g infotv infotv
WORKDIR /usr/src/app/infotv-tracon
COPY requirements.txt requirements-production.txt /usr/src/app/infotv-tracon/
RUN pip install --no-cache-dir -r requirements.txt -r requirements-production.txt -e ../infotv
COPY . /usr/src/app/infotv-tracon
RUN env DEBUG=1 python manage.py collectstatic --noinput && \
    python -m compileall -q .
USER infotv
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
