def print(*args, **kwargs):
    pass

def debug_print(*args, **kwargs):
    import builtins
    return builtins.print(*args, **kwargs)
