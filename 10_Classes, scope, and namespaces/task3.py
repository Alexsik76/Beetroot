# TV controller
class TVController:
    def __init__(self, chanels):
        self.chanels = chanels
        temp = dict(zip(range(1, len(self.chanels) + 1), self.chanels))
        self.dict_chanels = temp
        self.position = 1

    def last_channel(self):
        # turns on the last channel from the list.
        self.position = len(self.chanels)
        self.current_channel()

    def turn_channel(self, n):
        # turns on the N channel.
        self.position = n
        self.current_channel()

    def next_channel(self):
        if self.position == len(self.chanels):
            self.position = 1
        else:
            self.position += 1
        self.current_channel()

    def previous_channel(self):
        # turns on the previous channel.
        if self.position == 1:
            self.position = len(self.chanels)
        else:
            self.position -= 1
        self.current_channel()

    def current_channel(self):
        # returns the name of the current channel.
        print(self.dict_chanels[self.position])
        return self.dict_chanels[self.position]

    def is_exist(self, search_arg):
        if isinstance(search_arg, int):
            if int(search_arg) in self.dict_chanels.keys():
                ansver = True
            else:
                ansver = False
        elif search_arg in self.dict_chanels.values():
            ansver = True
        else:
            ansver = False
        if ansver:
            print('Yes')
        else:
            print('No')

    def first_channel(self):
        # turns on the first channel from the list.
        self.position = 1
        self.current_channel()


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)
controller.is_exist("BBC")
