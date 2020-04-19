def arg_rules(type_: type, max_length: int, contains: list):
    def args_(func):
        def wrapper(args):
            s = args
            check_list = []
            all_symbols = all(map(lambda x: True if x in s else False, contains))
            if isinstance(s, type_):
                check_list.append(True)
            else:
                check_list.append(False)
                print('Your value is not string!')
            if len(s) <= max_length:
                check_list.append(True)
            else:
                check_list.append(False)
                print(f'Your value length > {max_length}!')
            if all_symbols:
                check_list.append(True)
            else:
                check_list.append(False)
                print('Your an argument should contain ', *contains)
            if all(check_list):
                return func(s)
            else:
                return False

        return wrapper

    return args_


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
