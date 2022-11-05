def write_file(file_name, file_content):
    text_file = open(f'{file_name}.txt', mode='w', encoding='utf-8')
    text_file.write(file_content)
    pass

def append_file(file_name, append_content):
    text_file = open(f'{file_name}.txt', mode='a', encoding='utf-8')
    text_file.write(append_content)
    pass

def read_file(file_name):
    text_file = open(f'{file_name}.txt', encoding='utf-8')
    return text_file.read()
    pass
