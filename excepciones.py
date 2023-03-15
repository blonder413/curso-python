try:
    print(f'{5 / 0}')
except ZeroDivisionError as error:
    print(error)