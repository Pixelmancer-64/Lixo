import sys
import pathlib
import lz4.block
import json
import os

path = pathlib.Path.home().joinpath('.mozilla/firefox')
files = path.glob('*default*/sessionstore-backups/recovery.js*')


def save():
    urls = []
    for f in files:
        b = f.read_bytes()
        if b[:8] == b'mozLz40\0':
            b = lz4.block.decompress(b[8:])
        j = json.loads(b)
        for w in j['windows']:
            for t in w['tabs']:
                i = t['index'] - 1
                urls.append(t['entries'][i]['url'])

    print("você está com {urls} abas abertas".format(urls=len(urls)))

    for u in urls:
        os.system("echo '{urls}' >> ./salvooo.txt".format(urls=u))

    total = os.popen("cat salvooo.txt | wc -l").read()
    print(total)

    print("TUDO SALVO! Você já está com {urls} urls salvas no seu arquivo".format(
        urls=total.lower()))


def open():
    pass


while (True):
    option = input(
        ">>> Você deseja salvar (S) ou abrir (A) a última sessão salva? <<<")
    option = option.lower()
    if (option == 's'):
        save()
        break
    if (option == 'a'):
        open()
        break
