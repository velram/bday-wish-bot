from mastodon import Mastodon
import os


def get_toot():
    d = "வணக்கம் உலகே!"
    return d


if __name__ == '__main__':
    mastodon = Mastodon(
        #api_base_url=os.environ['MASTODON_API_BASE_URL'],
        #access_token=os.environ['MASTODON_ACCESS_TOKEN']
        api_base_url="https://masto.ai/",
        access_token="abcd"
    )
    mastodon.toot(get_toot())
