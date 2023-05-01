from unittest.mock import patch

from click.testing import CliRunner

from cli_gpt.cli import gpt


@patch('cli_gpt.cli.my_chat.call_gpt')
def test_cli_call_command_works_ok(mock_call_gpt):
    mock_call_gpt.return_value = ["I'm fine, thanks, and you?"]
    runner = CliRunner()
    result = runner.invoke(gpt, ['call', 'How are you?'])
    assert "I'm fine, thanks, and you?" in result.output


@patch('cli_gpt.cli.my_chat.call_gpt')
def test_cli_call_command_with_n_works_ok(mock_call_gpt):
    list_of_responses = [
        "I'm fine, thanks, and you?",
        "I'm very well, thanks, and you?",
        "I'm not to bad, thanks, and you?",
    ]
    mock_call_gpt.return_value = list_of_responses
    runner = CliRunner()
    result = runner.invoke(gpt, ['call', 'How are you?', '-n 3'])
    list_of_results = result.output.strip().split('\n')
    assert len(list_of_results) == 3
    assert list_of_results == list_of_responses
