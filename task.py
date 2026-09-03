class Task:
    def __init__(self, date, text, status, reward):
        self.date = date
        self.text = text
        self.status = status
        self.reward = reward

class Tasks:
    def __init__(self, taskList):
        self.collection = taskList

    def reward(self):
        result = 0

        for task in self.collection:
            if task.status == "Fertig":
                result += task.reward

        return result
    
        # return sum([task.reward for task in self.collection if task.status == 'Fertig'

if __name__ == '__main__':
    pass
    # test task classes