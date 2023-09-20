SRC_DIR = src
MAIN_FILE = main.py

run: 
	python3 $(SRC_DIR)/$(MAIN_FILE)

.PHONY: run
