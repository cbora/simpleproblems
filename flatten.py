
def flatten_list(iter):

    try:
        for item in iter:
            yield from flatten_list(item)
    except TypeError:
        yield iter
        
if __name__ == '__main__':
    inp = [[[1, 2, 3], [4, 5]], 6]
    res = list(flatten_list(inp))
    print(res)
