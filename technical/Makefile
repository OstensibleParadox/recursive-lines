# ===========================================
# MAKEFILE - Simple Commands for the Pipeline
# ===========================================
#
# Instead of remembering Python commands, just type:
#
#   make install     - Install Python dependencies
#   make all         - Run everything
#   make simulation  - Run agent simulation
#   make analyze     - Analyze stories
#   make dataset     - Build CSV (with HTML sanitization)
#   make clean       - Delete generated files
#   make help        - Show this help
#

.PHONY: all install simulation analyze dataset clean help

# Default: show help
help:
	@echo ""
	@echo "Available commands:"
	@echo "  make install     - Install Python dependencies"
	@echo "  make all         - Run the full pipeline"
	@echo "  make simulation  - Run agent simulation (slow, generates heatmap)"
	@echo "  make analyze     - Analyze story files"
	@echo "  make dataset     - Build CSV dataset (sanitizes HTML -> narrative)"
	@echo "  make clean       - Delete all generated files"
	@echo ""

install:
	pip install -r requirements.txt
	@echo "Dependencies installed (including beautifulsoup4 for HTML sanitization)."

all: install
	python run_pipeline.py --all

simulation:
	python run_pipeline.py --simulation

analyze:
	python run_pipeline.py --analyze

dataset:
	python run_pipeline.py --dataset

clean:
	rm -f results/*.png
	rm -f train.csv
	@echo "Cleaned generated files."
