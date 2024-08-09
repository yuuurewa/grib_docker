ARG PYTHON_VERSION=3.11.9

FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 unpack_grib.py
