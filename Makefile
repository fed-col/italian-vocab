# create and activate a virtual environment
venv:
	python3 -m venv venv
	. venv/bin/activate

# run main.py
run:
	python3 main.py

# format all files according to black
lint-all:
	python3 -m black .

# format a specific file according to black
lint:
	black $(FILE_NAME)

# install pip-tools
pip-tools:
	pip3 install pip-tools

# generate the requirements.txt file with pip-tools
reqs:
	python3 -m piptools compile --output-file=requirements.txt requirements.in --resolver=backtracking

# install packages listed in requirements.txt
install:
	python3 -m pip install -r requirements.txt

# return the names of any files that the program depends on
deps:
	@echo 'ita_eng_db.csv utils.py'

# run all the pytests in the repo
test:
	python3 -m pytest  

clean:
	@if [ -d "venv" ]; then \
		rm -rf venv; \
		echo "Removed venv directory"; \
	fi
	@if [ -f "requirements.txt" ]; then \
		rm -f requirements.txt; \
		echo "Removed requirements.txt file"; \
	fi

# show help
help:
	@echo "Please use 'make <target>' where <target> is one of the following:"
	@echo "  venv           create and activate a virtual environment"
	@echo "  run            run main.py"
	@echo "  lint-all       format all files according to black"
	@echo "  lint           format a specific file according to black (FILE_NAME required)"
	@echo "  pip-tools  	install pip-tools"
	@echo "  reqs           generate requirements.txt file with pip-tools"
	@echo "  install        install packages listed in requirements.txt"
	@echo "  deps           return the names of any files that the program depends on"
	@echo "  test			run all the pytests in the repository"
	@echo "  help           show this help message"
	@echo "  clean          remove generated files"
