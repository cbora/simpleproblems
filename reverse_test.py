


def reverse_x(x):
    pages = list(filter(None, x.split('\b')[::-1]))
    lines = [[' '.join(x.strip().split(' ')[::-1]) for x in list(filter(None, page.split('\n')))] for page in pages]
    out = ''
    for page in lines:
        out = '{}{}\\n\\b'.format(out, '\\n'.join(page))
    return out
    
    
if __name__ == '__main__':
    x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"
    out = reverse_x(x)
    print(out)
