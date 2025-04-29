# ┌─────────────────────────────────────────────┐
# │           🚀 Ingestion Stack Makefile       │
# └─────────────────────────────────────────────┘

.PHONY: up down logs status rebuild shell

# Load .env file
-include .env

up:
	docker-compose up --build -d

down:
	docker-compose down -v

rebuild:
	docker-compose down -v
	docker-compose up --build -d

logs:
	docker-compose logs -f

status:
	docker-compose ps

shell:
	docker exec -it mage /bin/bash

# ┌─────── Airflow Commands ───────┐

airflow-init:
	@echo "🛠️  Initializing Airflow DB and creating admin user..."
	docker-compose run --rm airflow airflow db init
	docker-compose run --rm airflow airflow users create \
		--username admin \
		--password admin \
		--firstname airflow \
		--lastname admin \
		--role Admin \
		--email admin@example.com

airflow-up:
	docker-compose up -d airflow airflow-scheduler postgres

airflow-down:
	docker-compose stop airflow airflow-scheduler

# ┌─────── Convenience Shortcuts ───────┐

jupyter:
	open http://localhost:8888

grafana:
	open http://localhost:3000

mage:
	open http://localhost:6789

jenkins:
	open http://localhost:8080

airflow:
	open http://localhost:8089

launchpad:
	open http://localhost:5000