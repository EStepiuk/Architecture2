import io


def get_string_from_serialyser(fileName="matches.json"):
    out = io.StringIO()
    with open(fileName, 'rt') as f:
        for line in f:
            out.write(line)

    return out
