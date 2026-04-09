"""
attractions.py - Данные об экскурсиях
"""

import random

ATTRACTIONS_DB = {
    "Сочи": [
        {"name": "Олимпийский парк", "desc": "Главная спортивная арена", "price": 500, "duration": "2-3ч", "icon": "🏟️", "rating": 4.9},
        {"name": "Сочи Парк", "desc": "Тематический парк", "price": 2500, "duration": "Весь день", "icon": "🎢", "rating": 4.8},
        {"name": "Красная Поляна", "desc": "Горный курорт", "price": 1500, "duration": "Весь день", "icon": "⛰️", "rating": 4.9},
        {"name": "Дендрарий", "desc": "Ботанический сад", "price": 300, "duration": "2-3ч", "icon": "🌳", "rating": 4.7},
        {"name": "Агурские водопады", "desc": "Живописные водопады", "price": 200, "duration": "3-4ч", "icon": "💧", "rating": 4.6}
    ],
    "Стамбул": [
        {"name": "Айя-София", "desc": "Византийский собор", "price": 1500, "duration": "2-3ч", "icon": "⛪", "rating": 4.9},
        {"name": "Голубая мечеть", "desc": "Действующая мечеть", "price": 0, "duration": "1-2ч", "icon": "🕌", "rating": 4.8},
        {"name": "Дворец Топкапы", "desc": "Резиденция султанов", "price": 1200, "duration": "3-4ч", "icon": "🏰", "rating": 4.9},
        {"name": "Прогулка по Босфору", "desc": "Круиз на корабле", "price": 800, "duration": "2ч", "icon": "🚢", "rating": 4.8},
        {"name": "Гранд-Базар", "desc": "Старейший крытый рынок", "price": 0, "duration": "2-3ч", "icon": "🛍️", "rating": 4.7}
    ],
    "Дубай": [
        {"name": "Бурдж Халифа", "desc": "Самое высокое здание", "price": 2000, "duration": "2ч", "icon": "🏙️", "rating": 4.9},
        {"name": "Дубай Молл", "desc": "Крупнейший ТЦ", "price": 0, "duration": "3-4ч", "icon": "🛍️", "rating": 4.8},
        {"name": "Сафари в пустыне", "desc": "Джип-сафари", "price": 4500, "duration": "5-6ч", "icon": "🏜️", "rating": 4.9},
        {"name": "Пальма Джумейра", "desc": "Искусственный остров", "price": 3000, "duration": "3ч", "icon": "🌴", "rating": 4.8},
        {"name": "Фонтан Дубая", "desc": "Танцующий фонтан", "price": 0, "duration": "30 мин", "icon": "💧", "rating": 4.9}
    ],
    "Пхукет": [
        {"name": "Острова Пхи Пхи", "desc": "Знаменитые острова", "price": 3000, "duration": "Весь день", "icon": "🏝️", "rating": 4.9},
        {"name": "Большой Будда", "desc": "45-метровая статуя", "price": 0, "duration": "1-2ч", "icon": "🙏", "rating": 4.7},
        {"name": "Слоновья деревня", "desc": "Этичный центр", "price": 2500, "duration": "3ч", "icon": "🐘", "rating": 4.8},
        {"name": "Старый Пхукет", "desc": "Китайско-португальская архитектура", "price": 0, "duration": "2-3ч", "icon": "🏘️", "rating": 4.6},
        {"name": "Ночной рынок", "desc": "Колоритные рынки", "price": 1000, "duration": "2-3ч", "icon": "🛍️", "rating": 4.7}
    ]
}


def get_attractions(city_name):
    """Получить экскурсии для города"""
    if city_name in ATTRACTIONS_DB:
        return ATTRACTIONS_DB[city_name]
    
    # Генерируем общие экскурсии
    return [
        {"name": f"Обзорная экскурсия по {city_name}", "desc": f"Лучшие достопримечательности {city_name}", "price": random.randint(800, 2000), "duration": "3-4ч", "icon": "🏛️", "rating": 4.7},
        {"name": f"Исторический центр {city_name}", "desc": f"Прогулка по старому городу", "price": random.randint(500, 1500), "duration": "2-3ч", "icon": "🏰", "rating": 4.6},
        {"name": f"Гастрономический тур по {city_name}", "desc": f"Дегустация местных блюд", "price": random.randint(1500, 3500), "duration": "3-4ч", "icon": "🍷", "rating": 4.8},
        {"name": f"Вечерний {city_name}", "desc": f"Ночная жизнь города", "price": random.randint(1000, 2500), "duration": "2-3ч", "icon": "🌙", "rating": 4.5},
        {"name": f"Природа вокруг {city_name}", "desc": f"Живописные окрестности", "price": random.randint(800, 2000), "duration": "4-5ч", "icon": "🌳", "rating": 4.6}
    ]