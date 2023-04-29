# A ChatGPT CLI Project 


The project's main goal is the creation of a CLI - Command Line Interface to allow Terminal users to interact with the 
chatGPT API.

## How it runs

After we install the project, we can execute the `gpt` command to see the help, like following:

```bash
$ gpt --help
Usage: gpt [OPTIONS] COMMAND [ARGS]...

  CLI from chatGPT This command line interface provides a pleasant terminal-
  based experience for ChatGPT.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  call  Make a question to chatGPT

```

There is a help about the sub command `call`, as following:

```bash
$ gpt call --help
Usage: gpt call [OPTIONS] PROMPT

  Make a question to chatGPT.

  The PROMPT is the question that you desire do to chatGPT.

Options:
  -n INTEGER  Inform the number of distinct responses you want, the default is 1.
  --help      Show this message and exit.

```

A simple example of use:
```bash
$ gpt call 'Who are Albert Einstein?'

Albert Einstein (1879–1955) was a German-born physicist who developed the theory of relativity and is generally 
considered one of the greatest scientists of all time. His work is also known for its influence on the philosophy of 
science. He received the 1921 Nobel Prize in Physics for his explanation of the photoelectric effect.

```