def arg_rules(type_: type, max_length: int, contains: list):
    def args_(func):
        def wrapper(args):
            s = args
            all_symbols = all(list(True if x in s else False for x in contains))
            no_characters = ', '.join(f'"{x}"' for x in contains if x not in s)
            check_dict = {
                'Your value is not string!': isinstance(s, type_),
                f'Your value length > {max_length}!': len(s) <= max_length,
                f'Your an argument should contain {no_characters}': all_symbols
            }
            if all(check_dict.values()):
                return func(s)
            else:
                alerts = list(x for x in check_dict if not check_dict[x])
                print(*alerts, sep='\n', end='.')
                return False

        return wrapper

    return args_


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
