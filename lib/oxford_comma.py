def oxford_comma(items):
    if len(items) < 3:
        return ' and '.join(items)
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]
