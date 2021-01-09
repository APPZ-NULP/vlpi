FROM python:3.8

ENV PROJECT_WORKDIR=/project
ENV DJANGO_SETTINGS_MODULE=vlpi.settings
ENV PYTHONUNBUFFERED 1

ADD requirements.txt $PROJECT_WORKDIR/requirements.txt

WORKDIR $PROJECT_WORKDIR
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc musl-dev && \
    pip install -r requirements.txt && \
    apt-get install -y gcc musl-dev netbase && \
    apt-get clean && \  
    rm -rf /var/lib/apt/lists/*
ADD . $PROJECT_WORKDIR

COPY docker-entrypoint.sh /

VOLUME [$PROJECT_WORKDIR]
EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
