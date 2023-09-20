SRC_DIR = src
MAIN_FILE = main.py

run:
	python3 $(SRC_DIR)/hangman/$(MAIN_FILE)

lint:
	flake8 $(SRC_DIR)

format:
	find $(SRC_DIR) -type f -name '*.py' | xargs autopep8 --in-place --aggressive --aggressive

.PHONY: run format
