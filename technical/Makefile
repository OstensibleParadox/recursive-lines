# ===========================================
# MAKEFILE - Simple Commands for the Pipeline
# ===========================================
#
# Instead of remembering Python commands, just type:
#
#   make all         - Run everything
#   make simulation  - Run agent simulation
#   make analyze     - Analyze stories
#   make dataset     - Build CSV
#   make clean       - Delete generated files
#   make help        - Show this help
#

.PHONY: all simulation analyze dataset clean help

# Default: show help
help:
	@echo ""
	@echo "Available commands:"
	@echo "  make all         - Run the full pipeline"
	@echo "  make simulation  - Run agent simulation (slow, generates heatmap)"
	@echo "  make analyze     - Analyze story files"
	@echo "  make dataset     - Build CSV dataset"
	@echo "  make clean       - Delete all generated files"
	@echo ""

all:
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
