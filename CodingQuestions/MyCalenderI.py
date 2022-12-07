class MyCalendar(object):

    def __init__(self):
        self.courses = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in range(len(self.courses)):
            if self.courses[i][0] > start:
                if i == 0:
                    if end <= self.courses[i][0]:
                        self.courses.insert(i, [start, end])
                        return True
                    else:
                        return False
                else:
                    if start >= self.courses[i - 1][1] and end <= self.courses[i][0]:
                        self.courses.insert(i, [start, end])
                        return True
                    else:
                        return False
        if len(self.courses) != 0 and start < self.courses[-1][1]:
            return False
        self.courses.append([start, end])
        return True