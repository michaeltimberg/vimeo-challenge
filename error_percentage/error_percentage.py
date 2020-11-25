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
    This script:
     1. Reads a log file line by line
     2. parses each line to obtain a timestamp, domain and HTTP status code
     3. Output the time interval for the log file and percent of 5xx errors per
        domain
    :param file_path: The relative path of the log file
    :return: Boolean if any exceptions were raised: for exit codes.
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

                end = e if (e := int(round(float(timestamp)))) > end else end
                start = s if (s := int(float(timestamp))) < start else start

                if not domains.get(domain, False):
                    domains[domain] = {'errors': 0, 'total': 0}
                domains[domain]['total'] += 1
                domains[domain]['errors'] += 1 if status_code[:1] == '5' else 0

        output = 'Between time {0} and time {1}:\n'.format(start, end)
        for domain_name, d in domains.items():
            output += f'{domain_name} returned ' \
                      f'{round((d["errors"] / d["total"]) * 100, 2):.2f}% ' \
                      f'5xx errors\n'

        print(output, end='')
        return True
    except Exception as error:
        exception(msg=error)
        return False


if __name__ == '__main__':
    exit(0 if bool(error_percentage()) else 1)
