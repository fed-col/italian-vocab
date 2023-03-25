# Italian Vocabulary Learning Tool

This is a tool to help you learn Italian vocabulary. The tool presents you with a random word in Italian and asks you to provide the English translation. It keeps track of your correct and incorrect answers and provides feedback after each guess. The vocabulary is stored in two text files (`ITA_vocab.txt` and `ENG_vocab.txt`) and can easily be edited or expanded.

## Requirements

The only requirement is `Python 3.x`, where `Python 3.6` is advised.

## Installation

To start using the tool on your machine, all you need to do is

1. Clone the repository to your local machine using git clone `https://github.com/your-username/italian-vocab.git`
2. Install the required dependencies by running `make install`.
> Note that `make` is UNIX only command. If you are working on a Windows machine, you should install using Chocolatey via `choco install make`, or similars.

## Usage

To start the program, run the following command in your terminal:

```bash
make run
```

This will launch the program and present you with the first word to translate. After each guess, the program will give you feedback and ask you to guess again.

To format all files according to the [Black](https://github.com/psf/black) code style, run:


```bash
make lint-all
```

To format a specific file according to the [Black](https://github.com/psf/black) code style, run:


```bash
make lint FILE_NAME=<name-of-file>
```

To list any dependencies that the program relies on, run:


```bash
make deps
```
