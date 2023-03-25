# run main.py
run:
	python3 main.py

# format all files according to black
lint-all:
	python3 -m black .

# format a specific file according to black
lint:
	black $(FILE_NAME)

# install piptools that are used down the line
install-pip-tools:
    pip3 install pip-tools

# generate the requirements.txt file with pip-tools
reqs:
	python3 -m piptools compile --output-file=requirements.txt requirements.in --resolver=backtracking

# install packages listed in requirements.txt
install:
	python3 -m pip install -r requirements.txt

# return the names of any files that the program depends on
deps:
	echo 'ITA_vocab.txt ENG_vocab.txt utils.py'  # replace with your actual dependencies

# show help
help:
	@echo "Please use 'make <target>' where <target> is one of the following:"
	@echo "  run            run main.py"
	@echo "  lint-all       format all files according to black"
	@echo "  lint           format a specific file according to black (FILE_NAME required)"
	@echo "  reqs           generate requirements.txt file with pip-tools"
	@echo "  install        install packages listed in requirements.txt"
	@echo "  deps           return the names of any files that the program depends on"
	@echo "  help           show this help message"
