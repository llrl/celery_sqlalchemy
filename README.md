# SQLAlchemy + Celery

It's a example application Celery + SQLAlchemy with (redis + sqlite) services


#### Setup

1. Setup services via docker-compose `docker-compose up -d`
2. Install requirements: `pip install -r requirements.txt`
3. Migrate: `python -m sql_alchemy migrate`
4. Run: `python -m sql_alchemy run`