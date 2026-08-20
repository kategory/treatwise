class Task:
    def __init__(self, date, text, status, reward):
        self.date = date
        self.text = text
        self.status = status
        self.reward = reward

class Tasks:
    def __init__(self, taskList):
        self.collection = taskList

if __name__ == '__main__':
    pass
    # test task classes