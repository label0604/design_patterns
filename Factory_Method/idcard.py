from framework import Factory, Product


class IDCard(Product):
    def __init__(self, owner):
        print('{owner}のカードを作ります。'.format(owner=owner))
        self.__owner = owner

    def use(self):
        print('{owner}のカードを使います。'.format(owner=self.__owner))

    def get_owner(self):
        return self.__owner


class IDCardFactory(Factory):
    def __init__(self):
        self.__owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.__owners.append(product.get_owner())

    def get_owners(self):
        return self.__owners
