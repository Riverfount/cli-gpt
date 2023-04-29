import click
import pkg_resources
from cli_gpt.config import settings
from cli_gpt.my_chat_gpt import MyChatGPT

my_chat = MyChatGPT(settings.OPENAI_API_KEY)


@click.group()
@click.version_option(pkg_resources.get_distribution('cli-gpt').version)
def main():
    """CLI from chatGPT
    This command line interface provides a pleasant terminal-based experience for ChatGPT.
    """


@main.command()
@click.argument('prompt')
@click.option('-n', type=int, default=1, help='Inform the number of distinct responses you want, the default is 1.')
def call(prompt, n):
    """Make a question to chatGPT.

    The PROMPT is the question that you desire do to chatGPT.
    """
    responses = my_chat.call_gpt(prompt, n=n)
    for i in range(n):
        click.echo(responses[i])
