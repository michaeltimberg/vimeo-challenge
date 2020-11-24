from click.testing import CliRunner
from error_percentage.error_percentage import error_percentage
# import error_percentage


# def test():
def test_reading_file():
    # error_percentage(file_path='../test/log_file.py')
    result = CliRunner().invoke(error_percentage, ['--file-path',
                                                   './test/log_sample.txt'])
    # print(dir(something))
    # print(something.exit_code)
    # print(something.output)

    # print(result.output)
    # print(result.output.splitlines().pop(0).split(' | ').pop(0))
    # assert False
    assert result.output.splitlines().pop(0) \
        .split(' | ').pop(0) == '1493969101.638'
    # assert True
