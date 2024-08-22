FROM python:3.12
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends tk-dev && rm -r /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install chromium
RUN playwright install-deps
RUN git config --global core.symlinks false
COPY . .
CMD ["python", "app.py"]