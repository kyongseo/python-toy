# FastAPI Authentication & CRUD with PostgreSQL

## 사용 스택 및 구성
  - 백엔드: Python 3.11, FastAPI, Uvicorn 
  - DB: PostgreSQL (Docker 컨테이너 기반)
  - ORM: SQLAlchemy 
  - DB Migration: Alembic 
  - 패키지 관리: uv-> 빠른 pip 대체 도구
  - 실행 환경: Docker + Docker Compose (WSL 기반)
  - 의존성 정의: pyproject.toml 기반, uv pip compile 사용

---
## 설정 및 실행
1. `uv init {uv-name}`
   - 새로운 uv 프로젝트 초기화
   - {uv-name} 폴더 생성 후 내부 구조
   - {uv-name}/
     ├── .python-version
     ├── .gitignore
     ├── pyproject.toml
     ├── main.py
     └── README.md
   - .python-version : 파이썬 버전 고정
   - pyproject.toml : 의존성 및 프로젝트 메타데이터 정의
   - .venv : 의존성을 추가하면 자동 생성

2. 명령어
    - `uv run`

---

## API 문서
FastAPI의 내장 문서를 통해 API를 테스트할 수 있습니다.

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 주요 명령어
1. make service-build
   - ocker Compose를 사용하여 모든 서비스를 빌드합니다.
2. make service-up
   - Docker Compose를 사용하여 모든 서비스를 백그라운드에서 실행합니다.
3. make service-down
   - Docker Compose를 사용하여 실행 중인 모든 서비스를 중지합니다.
4. make service-clean
   - Docker Compose를 사용하여 실행 중인 서비스를 중지하고, 모든 볼륨 데이터를 삭제합니다.
5. make api-up
   - FastAPI 애플리케이션 컨테이너(app)를 시작합니다.
6. make api-down
   - FastAPI 애플리케이션 컨테이너(app)를 중지합니다.
7. make api-restart
   - FastAPI 애플리케이션 컨테이너(app)를 재시작합니다.
8. make api-log
   - FastAPI 애플리케이션(app)의 로그를 실시간으로 확인합니다.