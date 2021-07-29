import os
import shutil
from typing import List, Dict
import py7zr
import click
import patoolib

from pyunpack import Archive

from cropper import process


def get_files(path) -> Dict[str, List]:
    files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        files[dirpath] = filenames

    return files


def export(filename: str, file_list: List[str]):
    filename = filename.replace('cbr', 'cbz')
    with py7zr.SevenZipFile(filename, 'w') as z:
        for file in file_list:
            z.write(file, file.replace('outbox/', ''))


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
    inbox = 'inbox'
    Archive(source).extractall(inbox)

    files = get_files(inbox)

    for path, names in files.items():
        if not len(names):
            continue

        path = path.replace('\\', '/') + '/'
        exportable = []
        for name in names:
            exportable.append(process(path, name, margin))

    export(outpath, exportable)

    reset_dirs()


if __name__ == "__main__":
    main()
