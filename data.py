from Sprint_6.locators.order_page_locators import OrderPageLocators

QUESTIONS_AND_ANSWERS = [
    (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (1,
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (2,
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (5,
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]

ORDER_DATA_1 = {
    "name": "Иван",
    "last_name": "Иванов",
    "address": "улица Пушкина, дом 9",
    "phone_number": "77778889900",
    "station_locator": OrderPageLocators.METRO_STATION_CHERKIZOVSKAYA,
    "delivery_date": "12.12.2022",
    "scooter_color": OrderPageLocators.SCOOTER_COLOR_BLACK,
    "rental_period": OrderPageLocators.RENTAL_PERIOD_TWO_DAYS
}

ORDER_DATA_2 = {
    "name": "Сергей",
    "last_name": "Сергеев",
    "address": "улица Ленина, дом 7",
    "phone_number": "79998887771",
    "station_locator": OrderPageLocators.METRO_STATION_LUBYANKA,
    "delivery_date": "10.10.2020",
    "scooter_color": OrderPageLocators.SCOOTER_COLOR_GREY,
    "rental_period": OrderPageLocators.RENTAL_PERIOD_FIVE_DAYS
}


class Urls:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"
