from gendiff.formatters.stylish import gen_stylish_diff

__all__ = ('get_formatter',)


def get_formatter(output_format):
    formatters = {
        'stylish': gen_stylish_diff
    }
    return formatters.get(output_format, None)
