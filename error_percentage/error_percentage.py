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
        domains = {}
        end = 0
        start = 2147483648

        with open(buffering=1, file=file_path,
                  mode='rt', encoding='utf8') as file:
            for line in file:
                [timestamp, _, domain, _, status_code] = line.split(' | ')[0:5]

                timestamp = int(round(float(timestamp)))
                end = timestamp if timestamp > end else end
                start = timestamp if timestamp < start else start

                if not domains.get(domain, False):
                    domains[domain] = {'errors': 0, 'total': 0}
                domains[domain]['total'] += 1
                domains[domain]['errors'] += 1 if status_code[:1] == '5' else 0

        print(start, end, sep='\n')
        [print(name, domain.get('errors'), domain.get('total'), sep='\n')
         for (name, domain) in domains.items()]
        return True
    except Exception as error:
        exception(msg=error)
        return False


if __name__ == '__main__':
    exit(0 if bool(error_percentage()) else 1)
