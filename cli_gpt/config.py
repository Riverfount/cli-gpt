from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='CLI_GPT',
    settings_files=[
        'cli_gpt/configs/settings.toml',
        'cli_gpt/configs/.secrets.toml',
    ],
    environments=True,
)
