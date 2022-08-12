FROM python:3.9-alpine AS base

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.9-alpine AS target
WORKDIR /app
COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV ENV_FILE=/env/.env

EXPOSE 8080

COPY app.py /app
ADD /templates /app/templates
CMD ["python", "app.py"]



