# Italian Vocabulary Learning Tool

This is an interactive tool to revise vocabulary, available in two languages: Italian and English. This tool reads data from a csv file, which contains a list of words in both languages. The user will be given a word in one language and will have to translate it into the other language. The user will have three attempts per word.

## Prerequisites

Before starting, please make sure you have `Python 3.7.1` or higher installed on your machine.

## Installation

To start using the tool on your machine, all you need to do is

1. Clone the repository to your local machine using `git clone https://github.com/fed-col/italian-vocab.git`
2. Open your terminal and navigate to the directory where the repository is located.
3. Run the following command to install the required packages: `make install`. If you are thrown an error make sure you have `pip-tools` installed using `make pip-tools`. Also make sure that you have the requiremnt.txt file via running `make reqs`.
> Please note that the `make` command is a UNIX-specific command. If you are working on a Windows machine, you may need to install it using a package manager like Chocolatey via the command `choco install make`, or a similar alternative.
4. Run the following command to start the program: `make run`.

## Usage

Upon running the program, the user will be greeted with a message and will be asked to choose the language they would like to translate from, either ITA or ENG. The user's response will be validated and the language to translate into will be set accordingly.

After the language has been selected, the program will read the vocabulary database file and the user will be prompted to translate each word. The user will have three attempts per word. If the user answers correctly, they will be prompted to continue or stop. If they answer incorrectly, the program will provide the correct answer and ask if the user wants to continue or stop.

Once the user has finished revising, the program will print a message congratulating the user on revising words and will tell a joke to amuse the user.

## Makefile Targets

The following targets are available in the `Makefile`:

* `run`: Run the program.
* `lint-all`: Format all files according to black.
* `lint`: Format a specific file according to black (FILE_NAME required).
* `pip-tools`: Install pip-tools.
* `reqs`: Generate the requirements.txt file with pip-tools.
* `install`: Install packages listed in requirements.txt.
* `deps`: Return the names of any files that the program depends on.
* `help`: Show the help message.

## Built With

* [`Python 3.7.1`](https://www.python.org)
* [`Pyjokes 0.6.0`](https://pyjok.es) - A library for programming-related jokes.
* [`Pygame 2.3.0`](https://www.pygame.org/news) - A library for devloping games in Python.
