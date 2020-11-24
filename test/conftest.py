from logging import exception
from subprocess import DEVNULL, \
                       PIPE, \
                       run


def install_as_package():
    """
    Install the main script as a package for test accessibility.
    :param: None
    :return: None
    """
    arguments = ['pip', 'install', '.', '--log', 'LOG_FILE']

    return run(args=arguments,
               check=True,
               shell=False,
               stderr=PIPE,
               stdin=None,
               stdout=DEVNULL)


def pytest_configure():
    """
    Configure pytest before running tests.
    :param: None
    :return: None
    """
    try:
        install_as_package()
    except Exception as error:
        exception(msg=error)
