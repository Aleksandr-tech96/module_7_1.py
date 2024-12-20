class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # название продукта
        self.weight = weight  # общий вес товара
        self.category = category  # категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                content = file.readlines()
            return [line.strip() for line in content]
        except FileNotFoundError:
            return []

    def add(self, *products: Product):
        existing_names = {line.split(', ')[0] for line in self.get_products()}
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_names:
                    print(f'Продукт "{product.name}" уже есть в магазине')
                else:
                    file.write(f'{product}\n')

        existing_names.add(product.name)

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)

    print("Список продуктов в магазине:")
    for product in s1.get_products():
        print(product)