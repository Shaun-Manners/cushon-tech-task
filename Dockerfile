FROM ubuntu:latest

# Set the working directory to /src - where the test code volume will be mounted
WORKDIR /src

# Install required libraries
RUN apt update && apt install -y wget unzip python3 python3-pip python3-venv

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome*.deb

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.95/linux64/chromedriver-linux64.zip \
    && unzip -p /tmp/chromedriver.zip chromedriver-linux64/chromedriver > /usr/bin/chromedriver \
    && rm /tmp/chromedriver.zip \
    && chmod ugo+rx /usr/bin/chromedriver \
    && apt-mark hold google-chrome-stable

# Setup a virtual environment to install python packages
# and then install required Python packages
RUN python3 -m venv .venv \
    && . .venv/bin/activate \
    && .venv/bin/pip install pytest pytest-selenium selenium \
    && .venv/bin/pip install pytest-html pep8 pycodestyle requests\
    && .venv/bin/pip freeze > requirements.txt

ENV AIRPORT_GAP_API_TOKEN='xa3z9Bxwf1nTgN9rNMmGSJw5'
ENV TEST_REGION='integration'