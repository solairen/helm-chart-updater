FROM python:3.13.5-slim-bookworm

LABEL org.opencontainers.image.source="https://github.com/solairen/helm-chart-updater"
LABEL org.opencontainers.image.description="Update Chart.yaml file"
LABEL org.opencontainers.image.authors="Michał Oleszek michal@michaloleszek.com"
LABEL org.opencontainers.image.licenses=MIT
LABEL release=production

RUN pip install PyYAML PyGithub

COPY update_chart.py /action/update_chart.py

ENTRYPOINT ["python", "/action/update_chart.py"]
