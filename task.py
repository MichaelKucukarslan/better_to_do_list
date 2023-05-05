class Task:
    def __init__(self, name, date = None, estimated_time_to_finish = None, notes = None):
        self._name = name
        self.date = date
        self.estimated_time_to_finish = estimated_time_to_finish
        self.notes = notes
    
    # @staticmethod
    def set_name(self, change_to):
        self._name = change_to

    def __str__(self):
        return " I am named: %s \n Dated: %s \n Estimated Length: %s \n Notes: %s" % \
            (self._name, self.date, self.estimated_time_to_finish, self.notes)

    def __repr__(self) -> str:
        pass