from mastodon import Mastodon
from dotenv import dotenv_values, load_dotenv
from pathlib import Path  # python3 only
import os
env_path = Path('env/local.env')
load_dotenv(dotenv_path=env_path)


def get_toot():
    toot_text = ".env test | refactoring variables"
    return toot_text


if __name__ == '__main__':
    mastodon = Mastodon(
        api_base_url=os.environ['MASTODON_API_BASE_URL'],
        access_token=os.environ['MASTODON_ACCESS_TOKEN']
    )
    mastodon.toot(get_toot())

