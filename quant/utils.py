import subprocess
import re
from notion_client import Client
from dotenv import load_dotenv


def link2id(link):
    """
    turns "https://www.notion.so/GRE-Quant-Hard-ee91bb3b7ee4412c9fdcbdd21d20edf5?pvs=4"
    into "380c78c0-e0f5-4565-bdbd-c4ccb079050d"
    :param link: notion link
    :return: page id
    """
    l = link.split("-")[-1].split("?")[0]
    indices = [8, 12, 16, 20]
    parts = [l[i:j] for i, j in zip([0] + indices, indices + [None])]
    return "-".join(parts)