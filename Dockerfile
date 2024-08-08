FROM python:3.8.3-alpine
WORKDIR /glock/Dev/sdk-fbanalyze/api-eventlogger

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src ./src
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD [python, -m, cherrypy, app.py]
