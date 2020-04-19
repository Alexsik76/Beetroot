class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []


    @property
    def get_company(self):
        return self.company

    @get_company.setter
    def get_company(self, company):
        self.company = company

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company if self.boss.get_company == company else self.boss.get_company
        self.boss = boss

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, boss):
        if isinstance(boss, Boss):
            self.boss = boss
