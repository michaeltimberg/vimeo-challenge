from click.testing import CliRunner
from error_percentage.error_percentage import error_percentage


'''
def test_reading_file():
    result = CliRunner().invoke(error_percentage, ['--file-path',
                                                   './test/log_sample.txt'])

    assert result.output.splitlines().pop(0) \
        .split(' | ').pop(0) == '1493969101.638'
        '''


def test_log_comprehension():
    result = CliRunner().invoke(error_percentage, ['--file-path',
                                                   './test/log_sample.txt'])

    assert result.output.splitlines() == ['1493969102', '1493969102',
                                          'player.vimeo.com', '8', '24',
                                          'vimeo.com', '4', '10']
