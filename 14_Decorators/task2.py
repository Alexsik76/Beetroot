def stop_words(words: list):
    def stop(func):
        def wrapper(*args):
            s = func(*args)
            for word in words:
                s = s.replace(word, '*')
            return s

        return wrapper

    return stop


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Steve'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
