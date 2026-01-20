FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/solairen/helm-chart-updater"
LABEL org.opencontainers.image.description="Update Chart.yaml file"
LABEL org.opencontainers.image.authors="Michał Oleszek michal@michaloleszek.com"
LABEL org.opencontainers.image.licenses=MIT
LABEL release=production

RUN pip install --no-cache-dir PyYAML PyGithub

COPY src/ /action/src/
COPY update_chart.py /action/update_chart.py

ENTRYPOINT ["python", "/action/update_chart.py"]
