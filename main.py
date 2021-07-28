import os
import shutil
from typing import List, Dict
import py7zr
import click

from pyunpack import Archive

from cropper import process


def get_files(path) -> Dict[str, List]:
    files = {}
    for (dirpath, dirnames, filenames) in os.walk('inbox'):
        files[dirpath] = filenames

    return files


def export(filename):
    with py7zr.SevenZipFile(filename, 'w') as z:
        z.writeall('./outbox')


def reset_dirs():
    shutil.rmtree('inbox', True)
    shutil.rmtree('outbox', True)
    os.makedirs('inbox')
    os.makedirs('outbox')


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('outpath', type=click.Path())
@click.option('--margin', default=20, prompt='Margin in pixels to keep')
def main(source, outpath, margin=20):

    reset_dirs()
    Archive(source).extractall('inbox')

    files = get_files('inbox')

    for path, names in files.items():
        if not len(names):
            continue

        path = path.replace('\\', '/') + '/'
        processed = []
        for name in names:
            processed.append(process(path, name, margin))

    export(outpath)


if __name__ == "__main__":
    main()
