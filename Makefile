.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint: ## Run linters
	poetry run black ./src ./tests
	poetry run ruff check ./src ./tests
	poetry run pytest ./tests --dead-fixtures --dup-fixtures

.PHONY: test
test: ## Run tests
	poetry run pytest ./tests

.PHONY: run
run: ## Run application
	poetry run python -m src.main