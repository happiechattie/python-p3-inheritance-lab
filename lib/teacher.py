#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge = ['math']):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]