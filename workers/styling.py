from styles.color import appColors


def read_style(path: str):
    """
    reads the stylesheet file, maps the colors and returns the style ready for use in widgets
    :param path:
    :return:
    """
    try:
        f = open(path)
        data = f.read()
        return parse_stylesheet_data(data)
    except OSError as e:
        print("Reading file error", e)


def parse_stylesheet_data(sheet: str):
    """
    replaces the keys in a style with their representing colors and returns
    the updated stylesheet
    :param sheet:
    :return:
    """

    parsed_value = sheet
    color_keys = appColors.color_keys

    for key, color in color_keys.items():
        parsed_value = parsed_value.replace(key, color)

    return parsed_value
