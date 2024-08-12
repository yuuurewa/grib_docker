ARG PYTHON_VERSION=3.11.9

FROM python:${PYTHON_VERSION}-slim

WORKDIR /grib_docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python3 unpack_grib.py
