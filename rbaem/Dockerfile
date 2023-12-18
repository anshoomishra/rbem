FROM python:3.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y bash \
    && rm -rf /var/lib/apt/lists/*


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8000
# copy project
COPY . /app