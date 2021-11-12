FROM tiangolo/uvicorn-gunicorn:python3.8 AS base

WORKDIR /opt/electos/vanadium
COPY requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

COPY src/electos/vanadium/api ./api
COPY src/electos/vanadium/app ./app
COPY src/electos/vanadium/model ./model
RUN chmod -R ugo+rx .

FROM base AS runapp
RUN groupadd -r vanadium && useradd -r -g vanadium vanadium

USER vanadium
WORKDIR /opt/electos

ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080", "vanadium.app.main:get_application()"]
