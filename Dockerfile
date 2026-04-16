FROM python:3.11-slim

WORKDIR /app

# Зависимости първо (cache trick)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# После кода
COPY . .

# Non-root user
RUN useradd --no-create-home appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]