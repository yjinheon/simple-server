FROM python:3.12-slim

WORKDIR /app

# 먼저 uv 설치
RUN pip install --no-cache-dir uv

# pyproject.toml 복사
COPY pyproject.toml .
# uv를 사용하여 pyproject.toml에서 의존성 설치
RUN uv pip install --no-cache-dir .

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
