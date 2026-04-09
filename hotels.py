"""
hotels.py - Данные об отелях с локальными изображениями
"""

import random

# Аэропорты вылета
AIRPORTS_DEPARTURE = [
    {"code": "SVO", "name": "Шереметьево (SVO)"},
    {"code": "DME", "name": "Домодедово (DME)"},
    {"code": "VKO", "name": "Внуково (VKO)"},
    {"code": "ZIA", "name": "Жуковский (ZIA)"}
]

# Реальные отели по городам
REAL_HOTELS = {
    "Москва": [
        {"name": "Ararat Park Hyatt Moscow", "price": 48000, "stars": 5, "desc": "Роскошный отель в центре Москвы. Вид на Большой театр."},
        {"name": "Four Seasons Moscow", "price": 55000, "stars": 5, "desc": "Отель на Манежной площади. Историческое здание."},
        {"name": "Lotte Hotel Moscow", "price": 52000, "stars": 5, "desc": "Премиальный отель. Лучший СПА в городе."},
        {"name": "St. Regis Moscow", "price": 48000, "stars": 5, "desc": "Элегантный отель на Патриарших прудах."},
        {"name": "Moscow Marriott Grand", "price": 18000, "stars": 4, "desc": "Отель на Тверской. Рядом метро."},
        {"name": "Hilton Moscow Leningradskaya", "price": 16000, "stars": 4, "desc": "Отель в сталинской высотке."},
        {"name": "Radisson Blu Belorusskaya", "price": 14000, "stars": 4, "desc": "Отель рядом с Белорусским вокзалом."},
        {"name": "Ibis Moscow Centre", "price": 6500, "stars": 3, "desc": "Бюджетный отель в центре."},
        {"name": "Izmailovo Hotel", "price": 3500, "stars": 3, "desc": "Крупнейший отель Европы."},
        {"name": "Novotel Moscow City", "price": 12000, "stars": 4, "desc": "Отель в деловом центре Москва-Сити."}
    ],
    "Сочи": [
        {"name": "Grand Hotel Polyana", "price": 25000, "stars": 5, "desc": "Роскошный отель в горах Красной Поляны."},
        {"name": "Bridge Resort", "price": 22000, "stars": 5, "desc": "Отель с собственным пляжем и аквапарком."},
        {"name": "Mercure Sochi Center", "price": 11000, "stars": 4, "desc": "Современный отель в центре Сочи."},
        {"name": "Sea Galaxy Hotel", "price": 9500, "stars": 4, "desc": "Отель на первой линии у моря."},
        {"name": "Radisson Blu Resort", "price": 22000, "stars": 5, "desc": "Премиальный курорт."},
        {"name": "Hyatt Regency Sochi", "price": 20000, "stars": 5, "desc": "Элегантный отель на берегу моря."},
        {"name": "Park Inn by Radisson", "price": 8500, "stars": 4, "desc": "Уютный отель рядом с парком."},
        {"name": "Boutique Hotel Sochi", "price": 3800, "stars": 3, "desc": "Мини-отель в тихом центре."},
        {"name": "Zhemchuzhina Hotel", "price": 4500, "stars": 3, "desc": "Бюджетный вариант в центре."},
        {"name": "Rosa Khutor Grand Hotel", "price": 28000, "stars": 5, "desc": "Отель в Красной Поляне."}
    ],
    "Дубай": [
        {"name": "Burj Al Arab Jumeirah", "price": 120000, "stars": 5, "desc": "Самый роскошный отель мира. Форма паруса."},
        {"name": "Atlantis The Palm", "price": 55000, "stars": 5, "desc": "Отель на острове Пальма. Аквапарк."},
        {"name": "Armani Hotel Dubai", "price": 48000, "stars": 5, "desc": "Отель в Бурдж Халифа."},
        {"name": "Jumeirah Beach Hotel", "price": 42000, "stars": 5, "desc": "Отель в форме волны."},
        {"name": "Address Downtown", "price": 38000, "stars": 5, "desc": "Отель рядом с фонтанами."},
        {"name": "Rove Downtown", "price": 15000, "stars": 4, "desc": "Современный отель."},
        {"name": "Ibis Dubai", "price": 8000, "stars": 3, "desc": "Бюджетный вариант."},
        {"name": "Premier Inn Dubai", "price": 9000, "stars": 3, "desc": "Хороший бюджетный отель."},
        {"name": "Hilton Dubai Jumeirah", "price": 35000, "stars": 5, "desc": "Отель на пляже."},
        {"name": "Park Hyatt Dubai", "price": 40000, "stars": 5, "desc": "Роскошный курорт."}
    ],
    "Стамбул": [
        {"name": "Ciragan Palace Kempinski", "price": 55000, "stars": 5, "desc": "Бывший дворец султана."},
        {"name": "Four Seasons Bosphorus", "price": 48000, "stars": 5, "desc": "Роскошный отель с видом на пролив."},
        {"name": "Hagia Sophia Mansions", "price": 35000, "stars": 5, "desc": "Отель с видом на Айя-Софию."},
        {"name": "Swissotel The Bosphorus", "price": 32000, "stars": 5, "desc": "Современный отель с видом на Босфор."},
        {"name": "InterContinental Istanbul", "price": 28000, "stars": 5, "desc": "Отель в центре города."},
        {"name": "Sultanhan Hotel", "price": 15000, "stars": 4, "desc": "Уютный отель в историческом районе."},
        {"name": "DoubleTree by Hilton", "price": 12000, "stars": 4, "desc": "Современный отель."},
        {"name": "Holiday Inn Istanbul", "price": 10000, "stars": 4, "desc": "Бюджетный вариант."},
        {"name": "Istanbul Golden City", "price": 6000, "stars": 3, "desc": "Бюджетный отель в центре."},
        {"name": "Hotel Amira Istanbul", "price": 11000, "stars": 4, "desc": "Отель в османском стиле."}
    ],
    "Пхукет": [
        {"name": "Anantara Phuket", "price": 35000, "stars": 5, "desc": "Роскошный курорт на пляже."},
        {"name": "Rosewood Phuket", "price": 48000, "stars": 5, "desc": "Ультра-роскошный отель."},
        {"name": "The Shore at Katathani", "price": 32000, "stars": 5, "desc": "Виллы с частным бассейном."},
        {"name": "Holiday Inn Resort", "price": 18000, "stars": 4, "desc": "Идеально для семей с детьми."},
        {"name": "Centara Grand Beach", "price": 28000, "stars": 5, "desc": "Премиальный курорт."},
        {"name": "Amari Phuket", "price": 20000, "stars": 4, "desc": "Вид на море."},
        {"name": "Novotel Phuket", "price": 12000, "stars": 4, "desc": "Современный отель."},
        {"name": "Patong Beach Hotel", "price": 10000, "stars": 4, "desc": "Отель на пляже."},
        {"name": "Baan Laimai Beach Resort", "price": 9000, "stars": 4, "desc": "Бюджетный курорт."},
        {"name": "Andaman Embrace", "price": 11000, "stars": 4, "desc": "Уютный отель."}
    ]
}


def get_hotels_for_city(city_name):
    """Получить отели для города с локальными изображениями"""
    city_mapping = {
        "Москва": "Москва",
        "Сочи": "Сочи",
        "Стамбул": "Стамбул",
        "Дубай": "Дубай",
        "Пхукет": "Пхукет",
        "Бангкок": "Пхукет",
        "Турция": "Стамбул",
        "ОАЭ": "Дубай",
        "Таиланд": "Пхукет"
    }
    
    city_key = city_mapping.get(city_name, city_name)
    
    if city_key in REAL_HOTELS:
        hotels = REAL_HOTELS[city_key]
        # Добавляем путь к локальному изображению
        for hotel in hotels:
            filename = hotel['name'].replace(' ', '_').replace('★', '').replace('⭐', '').strip()
            hotel["image"] = f"/static/images/hotels/{filename}.jpg"
        return hotels
    
    # Если город не найден, генерируем отели
    hotels = []
    for i in range(10):
        stars = random.choice([3, 4, 5])
        price = random.randint(3000, 50000)
        name = f"{['Бюджетный', 'Комфортный', 'Премиальный'][stars-3]} {city_name} Hotel"
        
        hotels.append({
            "name": name,
            "price": price,
            "stars": stars,
            "desc": f"{['Бюджетный', 'Комфортабельный', 'Роскошный'][stars-3]} отель в центре {city_name}",
            "image": f"/static/images/hotels/default_{stars}_star.jpg"
        })
    
    return hotels