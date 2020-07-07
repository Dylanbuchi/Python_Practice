import re


def rearrange_name(name):
    # method does: firstName LastName to LastName firstName

    result = re.search(r"^([\w .]*) ([\w .]*)$", name)
    if result is None:
        return name
    
    return f"{result[2]} {result[1]}"
