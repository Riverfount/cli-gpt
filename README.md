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

  Make a question to chatGPT

Options:
  -n INTEGER  Inform the number of distinct responses you want.
  --help      Show this message and exit.

```