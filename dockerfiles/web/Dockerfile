FROM python:3.6
ENV PYTHONUNBUFFERED 1
MAINTAINER Dev Pixelwolf <dev@pixelwolf.com.br>

RUN groupadd -r django && useradd -r -g django django
RUN apt-get -y update

# Create media and static folders
RUN mkdir -p /app && \
    mkdir -p /app/static && \
    mkdir -p /app/media && \
    mkdir -p /app/assets

WORKDIR /app

# Copy and install pip requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy manage, entrypoint and pytest_run scripts
COPY ./manage_container.sh /manage_container.sh
COPY ./entrypoint.sh /entrypoint.sh

# Give scripts run permission
RUN chmod +x /entrypoint.sh && \
    chmod +x /manage_container.sh

# Update file owners
RUN chown -R django /app && \
    chown django /entrypoint.sh && \
    chown django /manage_container.sh && \
    chown django -R /app/static && \
    chown django -R /app/media && \
    chown django -R /app/assets
