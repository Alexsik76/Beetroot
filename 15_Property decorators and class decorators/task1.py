class RegistrationPage:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email if RegistrationPage.validate(email) else ''

    @classmethod
    def validate(cls, email: str) -> bool:
        """To validate parameter email, passed to the constructor"""

        def is_followed(string: str, spec_simb: list) -> bool:
            """ Return False if an underscore, period, or dash must
                are followed by one or more letter or number."""
            s1 = string
            for i in range(len(s1) - 1):
                if s1[i] in spec_simb:
                    if (i == 0) or not (s1[i + 1].isalnum() and s1[i - 1].isalnum()):
                        return True
                elif not s1[i].isalnum():
                    return True
            return False

        s = email
        dict_errors1 = {
            'The address is not contains "@"': s.count('@') == 0,
            'The address is contains more, then 1 "@"': s.count('@') > 1,
        }
        if any(dict_errors1.values()):
            list_errors1 = list(x for x in dict_errors1 if dict_errors1[x])
            print(*list_errors1, sep='\n', end='.')
            return False
        else:
            name, domain = s.split('@')[0], s.split('@')[1]
            dict_errors2 = {
                'Name is empty': len(domain) == 0,
                'Domain is empty': len(domain) == 0,
                'Must be followed by one or more letter or number.': is_followed(name, ['_', '.', '-']),
                'Allowed characters: letters, numbers, dashes': is_followed(domain, ['.', '-']),
                'The last portion of the domain must be at least two characters': not domain[-2:].isalpha(),
            }
            if any(dict_errors2.values()):
                list_errors2 = list(x for x in dict_errors2 if dict_errors2[x])
                print(*list_errors2, sep='\n', end='.')
                return False
        return True


y = RegistrationPage('Alex', 'alex@jurist.vn.ua')
print(y.email)
