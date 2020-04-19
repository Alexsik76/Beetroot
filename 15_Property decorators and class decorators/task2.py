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

    @property
    def get_workers(self):
        return self.workers

    @get_workers.setter
    def get_workers(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        assert isinstance(boss, Boss)
        self.get_boss = boss
        self.company = company if self.boss.get_company == company else self.boss.get_company

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, boss):
        if isinstance(boss, Boss):
            self.boss = boss
            self.boss.get_workers = self
        else:
            print(boss, 'is not instance off Boss.class')


b1 = Boss(1, 'Alex', 'IBM')
b2 = Boss(2, 'Ira', 'BMW')
w1 = Worker(11, 'Vova', 'IBN', b2)
print(b1.name, b1.get_company, b1.get_workers)
print(w1.name, w1.company, w1.get_boss.name)
w1.boss = b2
print(b2.name, b2.get_company, b2.get_workers[0].name)
