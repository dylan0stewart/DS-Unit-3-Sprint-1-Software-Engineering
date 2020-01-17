"""
Class Report: Part 4 of the Sprint Challenge
- Generate random Product list, and get an Inventory Report on that list
"""

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        # build the name of the product
        adj = sample(ADJECTIVES, 1)
        noun = sample(NOUNS, 1)
        name = adj[0] + ' ' + noun[0]

        # establish the other variables for the product
        price = randint(5, 100)
        weight = randint(5, 100)
        flamm = round(uniform(0, 2.5), 6)

        products.append(Product(name, price, weight, flamm))
    return products


def inventory_report(self):
    """
    Prints out an Inventory Report for a list of Products.
    """
    names = []
    prices = []
    weights = []
    flames = []
    # Loop over products list
    for x in self:
        names.append(x.name)
        prices.append(x.price)
        weights.append(x.weight)
        flames.append(x.flamm)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'There are {len(set(names))} unique products.')
    print(f'Average Price: ${round(sum(prices) / len(prices),2)}.')
    print(f'Average weight: {round(sum(weights) / len(weights), 2)} kgs.')
    print(f'Average Flammability {round(sum(flames) / len(flames), 2)}.')
    return names, prices, weights, flames


if __name__ == '__main__':
    inventory_report(generate_products())
