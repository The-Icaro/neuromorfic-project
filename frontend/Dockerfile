FROM python:3.10.10-slim AS base

WORKDIR /app

EXPOSE 8501

RUN apt-get update && apt-get install libgomp1

COPY Pipfile .
RUN pip install pipenv

FROM base AS dependencies
RUN pipenv install --system --skip-lock

FROM base AS development
RUN pipenv install --system --dev --skip-lock
COPY . .

ENV BACKEND_ROUTE=http://backend-backend-1:3000/app/storedata

CMD ["streamlit", "run", "main.py"]

FROM dependencies AS production
COPY . .
COPY main.py .