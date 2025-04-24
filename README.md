- 사용 스택 및 구성
  - 백엔드: Python 3.11, FastAPI, Uvicorn 
  - DB: PostgreSQL (Docker 컨테이너 기반)
  - ORM: SQLAlchemy 
  - DB Migration: Alembic 
  - 패키지 관리: uv-> 빠른 pip 대체 도구
  - 실행 환경: Docker + Docker Compose (WSL 기반)
  - 의존성 정의: pyproject.toml 기반, uv pip compile 사용

---

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