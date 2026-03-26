class Flowers:
    def __init__(self, name, color, stem_length, initial_freshness_days, life_span_days, price):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.initial_freshness_days = initial_freshness_days
        self.life_span_days = life_span_days
        self.price = price

    def is_currently_fresh(self):
        return self.initial_freshness_days > 3

    def __str__(self):
        status = "свежий" if self.is_currently_fresh() else "увядший"
        return (f"{self.name}: {self.color}, {self.stem_length}см, "
                f"состояние: {status}, "
                f"время жизни: {self.life_span_days} дней, "
                f"стоимость: {self.price} руб.,")


class Peony(Flowers):
    def __init__(self, color, stem_length, initial_freshness_days, life_span_days, price, aroma):
        super().__init__("Пион", color, stem_length, initial_freshness_days, life_span_days, price)
        self.aroma = aroma

    def __str__(self):
        return f"{super().__str__()} аромат: {self.aroma}"


class Tulip(Flowers):
    def __init__(self, color, stem_length, initial_freshness_days, life_span_days, price, is_double):
        super().__init__("Тюльпан", color, stem_length, initial_freshness_days, life_span_days, price)
        self.is_double = is_double

    def __str__(self):
        return f"{super().__str__()} край лепестка: {self.is_double}"


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        if isinstance(flower, Flowers):
            self.flowers.append(flower)
        else:
            print("Можно добавлять только объекты класса Flower или его наследников.")

    def calculate_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def get_average_life_span(self):
        if not self.flowers:
            return 0
        average_life = sum(flower.life_span_days for flower in self.flowers) / len(self.flowers)
        return average_life

    def sort_flowers(self, param="life_span_days"):
        if param == "life_span_days":
            self.flowers.sort(key=lambda flower: flower.life_span_days, reverse=True)
        elif param == "color":
            self.flowers.sort(key=lambda flower: flower.color)
        elif param == "stem_length":
            self.flowers.sort(key=lambda flower: flower.stem_length, reverse=True)
        elif param == "price":
            self.flowers.sort(key=lambda flower: flower.price, reverse=True)
        elif param == "initial_freshness_days":
            self.flowers.sort(key=lambda flower: flower.initial_freshness_days, reverse=True)
        else:
            print(f"Неизвестный параметр сортировки: {param}")

    def find_flowers_by_life_span(self, min_life_span=5):
        if not self.flowers:
            return []

        find_flowers = []
        for flower in self.flowers:
            if flower.life_span_days >= min_life_span:
                find_flowers.append(flower)
        return find_flowers

    def __str__(self):
        if not self.flowers:
            return "Букет пустой."
        bouquet_str = "Букет:\n"
        for flower in self.flowers:
            bouquet_str += f"- {flower}\n"
        bouquet_str += f"\nОбщая стоимость: {self.calculate_total_price()} руб.\n"
        bouquet_str += f"Среднее время жизни цветов: {self.get_average_life_span():.2f} дней.\n"
        return bouquet_str


peony1 = Peony(color="красный", stem_length=60, initial_freshness_days=4, life_span_days=6, price=15, aroma="легкий")
peony2 = Peony(color="бежевый", stem_length=55, initial_freshness_days=2, life_span_days=5, price=13, aroma="яркий")
tulip1 = Tulip(color="белый", stem_length=40, initial_freshness_days=3, life_span_days=7, price=4, is_double="махровый")
tulip2 = Tulip(color="фиолетовый", stem_length=45, initial_freshness_days=1, life_span_days=8, price=5,
               is_double="гладкий")
peony3 = Peony(color="розовый", stem_length=70, initial_freshness_days=3, life_span_days=9, price=18, aroma="легкий")

my_bouquet = Bouquet()
my_bouquet.add_flower(peony1)
my_bouquet.add_flower(tulip1)
my_bouquet.add_flower(peony2)
my_bouquet.add_flower(tulip2)
my_bouquet.add_flower(peony3)

print(my_bouquet)

print("Поиск цветов с временем жизни >= 6 дней")
long_lived_flowers = my_bouquet.find_flowers_by_life_span(min_life_span=6)
if long_lived_flowers:
    for flower in long_lived_flowers:
        print(f"- {flower.name}: {flower.life_span_days} дней")
else:
    print("Цветы с таким временем жизни не найдены.")

print("\nБукет, отсортированный по стоимости")
my_bouquet.sort_flowers("price")
for flower in my_bouquet.flowers:
    print(f"- {flower.name}: {flower.color} - {flower.price} руб")
