from logging import exception

import click


@click.command()
@click.option('--file-path',
              '-f',
              help='Relative path to log file.',
              required=True,
              type=str)
def error_percentage(file_path):
    """
    Hopefully, when complete, this script will:
     1. Read input file in chunks
     2. Read chunks line by line
     3. TODO
    :param file_path:
    :return: Boolean if any exceptions were raised.  For exit codes.
    :raise OSError:  if the file path is invalid or if the file cannot be read.
    """
    try:
        with open(buffering=1, file=file_path,
                  mode='rt', encoding='utf8', ) as file:
            [print(line, end='') for line in file]
    except Exception as error:
        exception(msg=error)
        return False


if __name__ == '__main__':
    exit(0 if bool(error_percentage()) else 1)
