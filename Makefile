# Makefile generated with pymakefile
help:
	@grep -E '^[A-Za-z0-9_.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "[36m%-30s[0m %s\n", $$1, $$2}'

r:
	docker compose up -d

t:  ## Run tests
	docker compose run --no-deps --rm api pytest --cov='app'

lint:  ## Fix linter errors
	docker compose run --rm api sh -c "black . && isort . --profile black && flake8 ."

lint-check:  ## Run linter
	docker-compose run --no-deps --rm api black . --check
	docker-compose run --no-deps --rm api isort . --check-only --profile black
	docker-compose run --no-deps --rm api flake8 .