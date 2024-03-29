import json
from datetime import datetime
from datetime import timedelta
from pathlib import Path

try:
    from pytablewriter import MarkdownTableWriter
except ImportError as error:
    print(f'module not found - {error}')

md = []
line = []
writer = MarkdownTableWriter()
writer.headers = ['bookmarks', 'date']
home = str(Path.home())
fullpath = home + '/.config/vivaldi/Default/Bookmarks'


def get_time(dtms):
    seconds, micros = divmod(dtms, 1000000)
    days, seconds = divmod(seconds, 86400)
    dtime = datetime(1601, 1, 1) + timedelta(days, seconds, micros)
    return dtime.strftime('%c')


with open(fullpath) as book:
    jsondict = json.loads(book.read())
    blist = jsondict['roots']['bookmark_bar']['children']
    for element in blist:
        line.append(f"{get_time(int(element.get('date_added')))}")
        line.append(f"[{element.get('name')}]({element.get('url')})")
        md.append(line)
        line = []

writer.value_matrix = md
with open('bookmarks.md', 'w+') as of:
    of.write(writer.dumps())
