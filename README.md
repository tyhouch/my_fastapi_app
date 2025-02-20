cd my_fastapi_app
source venv/bin/activate   # (or venv\Scripts\activate on Windows)
uvicorn main:app --host 0.0.0.0 --port 8000

Then open http://localhost:8000/health or http://localhost:8000/simple_generate to test.
