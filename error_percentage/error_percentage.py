from logging import exception

import click


@click.command()
@click.option('--end-timestamp',
              '-e',
              help='End time, expressed as a Unix epoch timestamp',
              required=True,
              type=int)
@click.option('--file-path',
              '-f',
              help='Relative path to log file.',
              multiple=True,
              required=True,
              type=str)
@click.option('--start-timestamp',
              '-s',
              help='Start time, expressed as a Unix epoch timestamp',
              required=True,
              type=int)
def error_percentage(
    end_timestamp,
    file_path,
    start_timestamp
):
    """
    This script:
     1. Reads a log file line by line
     2. parses each line to obtain a timestamp, domain and HTTP status code
     3. Output the time interval for the log file and percent of 5xx errors per
        domain
    :param end_timestamp: End time, expressed as a Unix epoch timestamp.
    :param file_path: The relative path of the log file
    :param start_timestamp: Start time, expressed as a Unix epoch timestamp.
    :return: Boolean if any exceptions were raised: for exit codes.
    :raise OSError:  if the file path is invalid or if the file cannot be read.
    """
    try:
        domains = {}

        for file in list(file_path):
            with open(buffering=1, file=file,
                      mode='rt', encoding='utf8') as log_file:
                for line in log_file:
                    [timestamp,
                     _,
                     domain,
                     _,
                     status_code] = line.split(' | ')[0:5]

                    if (int(float(timestamp)) < start_timestamp
                            or int(float(timestamp)) >= end_timestamp):
                        continue

                    if not domains.get(domain, False):
                        domains[domain] = {'errors': 0, 'total': 0}
                    domains[domain]['total'] += 1
                    domains[domain]['errors'] += 1 \
                        if status_code[:1] == '5' else 0

        output = 'Between time {0} and time {1}:\n'.format(start_timestamp,
                                                           end_timestamp)
        for domain_name, d in domains.items():
            output += f'{domain_name} returned ' \
                      f'{round((d["errors"] / d["total"]) * 100, 2):.2f}% ' \
                      f'5xx errors\n'

        if not bool(domains):
            output += 'No 5xx errors were returned!\n'

        print(output, end='')
        return True
    except Exception as error:
        exception(msg=error)
        return False


if __name__ == '__main__':
    exit(0 if bool(error_percentage()) else 1)
