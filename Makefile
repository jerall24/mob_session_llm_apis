.PHONY: help setup venv install clean run-1 run-2 run-3

# Default Python interpreter
PYTHON := python3
VENV := venv
BIN := $(VENV)/bin

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: venv install ## Complete setup: create venv and install dependencies
	@echo ""
	@echo "✓ Setup complete!"
	@echo ""
	@echo "To activate the virtual environment, run:"
	@echo "  source venv/bin/activate"
	@echo ""

venv: ## Create Python virtual environment
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		$(PYTHON) -m venv $(VENV); \
		echo "✓ Virtual environment created"; \
	else \
		echo "✓ Virtual environment already exists"; \
	fi

install: venv ## Install Python dependencies
	@echo "Installing dependencies..."
	@$(BIN)/pip install --upgrade pip
	@$(BIN)/pip install -r requirements.txt
	@echo "✓ Dependencies installed"

clean: ## Remove virtual environment and generated files
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@rm -f output.json
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@echo "✓ Cleanup complete"
