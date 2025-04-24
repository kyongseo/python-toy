FROM python:3.11-slim

WORKDIR /usr/src/app

# psycopg2 설치를 위한 빌드 툴 설치
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# uv 설치
RUN pip install uv

# pyproject.toml만 복사 후 requirements.txt 생성
COPY pyproject.toml ./
RUN uv pip compile pyproject.toml > requirements.txt

# requirements.txt 복사 및 설치
COPY requirements.txt ./
RUN uv pip install --system --requirements=requirements.txt && \
     pip install psycopg2-binary
# 명시적으로 설치 추가

# 전체 코드 복사
COPY . .

# uvicorn 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
