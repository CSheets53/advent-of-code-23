def read_file_strings(input_filename: str):
    lines = []
    with open(f"./inputs/{input_filename}.txt", 'r') as f:
        lines = f.read().splitlines()

    return lines
