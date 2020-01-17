"""
Classes for Acme Products: Parts 1-3 of the Sprint Challenge
"""

import random

# Part 1: Keepin it Classy!


class Product:
    def __init__(self, name, price=10, weight=20, flamm=.5):
        '''
        Product Class for Acme-
        Assigns-
            name(str): name of product
            price(int): price of product
            weight(int): weight of product
            flamm(float): flammability of product
            identifier(int): random integer using random.randint
                             between 1000000 & 99999999
        '''
        self.name = name
        self.price = price
        self.weight = weight
        self.flamm = flamm
        self.identifier = random.randint(1000000, 9999999)

# Part 2: Objects that Go!

    def stealability(self):
        """
        theft_risk is the price of a product divided by it's weight.
        There are 3 possible outputs determined by their theft risk:
            1. theft_risk is less than .5: 'Not So Stealable...'
            2. theft_risk is greater than or equal to .5 but less than 1: 'Kinda Stealable.'
            2. theft_risk is greater than or equal to 1: 'Very Stealable!'
        """
        theft_risk = (self.price / self.weight)
        if theft_risk < 0.5:
            return 'Not So Stealable...'
        elif theft_risk >= 0.5 and theft_risk < 1:
            return 'Kinda Stealable.'
        return 'Very Stealable!'

    def explode(self):
        """
        boomability is the flammability of a product multiplied by its weight.
        There are 3 possible outputs determined by the boomability factor:
            1. boomability is less than 10: '...fizzle'
            2. boomability is greater than or eqaul to 10 but less than 50: '...boom!'
            3. boomability is greater than or equal to 50: '...BABOOM!'
        """
        boomability = (self.flamm * self.weight)
        if boomability < 10:
            return '...fizzle'
        elif boomability >= 10 and boomability < 50:
            return '...boom!'
        return '...BABOOM!'

# Part 3: A proper Inheritance


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flamm=.5):
        super().__init__(name, price, weight, flamm)

    def explode(self):
        '''
        Override the 'explode' method from Product class, always return "...It's a glove"
        for the BoxingGlove.
        '''
        return "...It's a glove."

    def punch(self):
        '''
        punch() has 3 possible outputs:
            1. weight < 5: 'That Tickles.'
            2. 5 =< weight <15: 'Hey that hurt!'
            3. weight > 15: 'OUCH!'
        '''
        if self.weight < 5:
            return "That Tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        return "OUCH!"
