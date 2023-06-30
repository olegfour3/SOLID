Концепция SOLID представляет собой набор принципов объектно-ориентированного программирования, которые способствуют созданию гибких, расширяемых и понятных программных систем. В файле solid.py пример кода на Python, демонстрирующий применение принципов SOLID.


В данном примере применены различные принципы SOLID:

1. Принцип единственной ответственности: Каждый класс отвечает только за одну задачу. Shape - определяет интерфейс для всех геометрических фигур, Rectangle, Circle, Square, Sphere - представляют конкретные реализации геометрических фигур, AreaCalculator - вычисляет общую площадь фигур, VolumeCalculator - вычисляет общий объем трехмерных фигур.
2. Принцип открытости/закрытости: Классы Rectangle, Circle, Square, Sphere можно легко расширить для добавления новых типов фигур, не изменяя существующий код.
3. Принцип подстановки Барбары Лисков: Класс Square является подтипом класса Rectangle и может быть использован везде, где ожидается объект типа Rectangle, не нарушая корректность программы.
4. Принцип разделения интерфейса: Интерфейсы Shape и ThreeDimensionalShape содержат только методы, которые соответствуют их предназначению, и клиенты могут зависеть только от интерфейсов, которые они используют.
5. Принцип инверсии зависимостей: Классы AreaCalculator и VolumeCalculator зависят от абстракций (Shape и ThreeDimensionalShape), а не от конкретных реализаций, что обеспечивает гибкость и возможность замены реализаций фигур без изменения кода этих классов.



___
# 1) Принцип единственной ответственности (Single Responsibility Principle)
## Классы должны иметь только одну причину для изменения.

```python
# Пример: Система управления товарами в интернет-магазине

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductRepository:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)


class ProductDiscountCalculator:
    def calculate_discount(self, product):
        if product.price > 100:
            return product.price * 0.1  # Скидка 10%
        return 0


# Использование кода

repository = ProductRepository()
discount_calculator = ProductDiscountCalculator()

product1 = Product("Phone", 150)
product2 = Product("Headphones", 80)

repository.add_product(product1)
repository.add_product(product2)

for product in repository.products:
    discount = discount_calculator.calculate_discount(product)
    discounted_price = product.price - discount
    print(f"{product.name}: Price - {product.price}, Discount - {discount}, Discounted Price - {discounted_price}")
```

В этом примере класс ***Product*** представляет товар с его именем и ценой. Класс ***ProductRepository*** отвечает за хранение и управление товарами, позволяя добавлять и удалять товары. Класс ***ProductDiscountCalculator*** рассчитывает скидку на товары в зависимости от их цены. Каждый класс имеет только одну причину для изменения и можно легко расширить, добавив новые методы или функциональность, не изменяя существующий код.


___
# 2) Принцип открытости/закрытости (Open/Closed Principle)
## Программные сущности должны быть открыты для расширения, но закрыты для изменения.

```python
# Пример: Система обработки платежей в интернет-магазине

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Логика обработки платежа с использованием кредитной карты
        print(f"Processing credit card payment for amount: {amount}")


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Логика обработки платежа с использованием PayPal
        print(f"Processing PayPal payment for amount: {amount}")


class Order:
    def __init__(self, amount, payment_processor):
        self.amount = amount
        self.payment_processor = payment_processor

    def process_order(self):
        self.payment_processor.process_payment(self.amount)


# Использование кода

credit_card_processor = CreditCardPaymentProcessor()
paypal_processor = PayPalPaymentProcessor()

order1 = Order(100, credit_card_processor)
order1.process_order()

order2 = Order(50, paypal_processor)
order2.process_order()


class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Логика обработки платежа с использованием Stripe
        print(f"Processing Stripe payment for amount: {amount}")


order3 = Order(75, StripePaymentProcessor())
order3.process_order()
```
В этом примере классы ***CreditCardPaymentProcessor*** и ***PayPalPaymentProcessor*** представляют различные способы обработки платежей в интернет-магазине. Класс ***Order*** принимает объект, реализующий абстрактный класс ***PaymentProcessor***, в качестве зависимости для обработки платежей. Это позволяет легко добавлять новые способы обработки платежей, создавая новые классы, реализующие ***PaymentProcessor***, без изменения существующего кода класса ***Order***.

Таким образом, принцип открытости/закрытости соблюдается, поскольку система готова к расширению путем добавления новых классов, но при этом она остается закрытой для изменений в существующем коде.


___
# 3) Принцип подстановки Барбары Лисков (Liskov Substitution Principle)
## Объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения корректности программы.

```python
# Пример: Система оплаты заказов в интернет-магазине

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Логика обработки платежа с использованием кредитной карты
        print(f"Processing credit card payment for amount: {amount}")


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Логика обработки платежа с использованием PayPal
        print(f"Processing PayPal payment for amount: {amount}")


class Order:
    def __init__(self, amount, payment_processor):
        self.amount = amount
        self.payment_processor = payment_processor

    def process_order(self):
        self.payment_processor.process_payment(self.amount)


# Использование кода

credit_card_processor = CreditCardPaymentProcessor()
paypal_processor = PayPalPaymentProcessor()

order1 = Order(100, credit_card_processor)
order1.process_order()

order2 = Order(50, paypal_processor)
order2.process_order()
```

В этом примере классы ***CreditCardPaymentProcessor*** и ***PayPalPaymentProcessor*** являются подтипами абстрактного класса ***PaymentProcessor***, и они могут быть использованы вместо него без изменения корректности программы. Класс ***Order*** представляет заказ с определенной суммой и определенным процессором оплаты. Это позволяет гибко выбирать различные методы оплаты и подменять их в зависимости от потребностей.



___
# 4) Принцип разделения интерфейса (Interface Segregation Principle)
## Клиенты не должны зависеть от интерфейсов, которые они не используют.

```python
# Пример: Система уведомлений для пользователей

from abc import ABC, abstractmethod


class EmailNotifier(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass


class SMSNotifier(ABC):
    @abstractmethod
    def send_sms(self, recipient, message):
        pass


class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class UserNotificationService:
    def __init__(self, email_notifier, sms_notifier):
        self.email_notifier = email_notifier
        self.sms_notifier = sms_notifier

    def send_notification(self, user, message):
        if self.email_notifier and isinstance(self.email_notifier, EmailNotifier):
            self.email_notifier.send_email(user.email, "Notification", message)
        if self.sms_notifier and isinstance(self.sms_notifier, SMSNotifier):
            self.sms_notifier.send_sms(user.phone, message)


# Использование кода

class EmailSender(EmailNotifier):
    def send_email(self, recipient, subject, message):
        print(f"Sending email to: {recipient}, Subject: {subject}, Message: {message}")


class SMSSender(SMSNotifier):
    def send_sms(self, recipient, message):
        print(f"Sending SMS to: {recipient}, Message: {message}")


user1 = User("John", "john@example.com", "+1234567890")
user2 = User("Alice", "alice@example.com", "+9876543210")

email_sender = EmailSender()
sms_sender = SMSSender()

notification_service = UserNotificationService(email_sender, sms_sender)

notification_service.send_notification(user1, "Hello, John!")
notification_service.send_notification(user2, "Hello, Alice!")
```

В этом примере классы ***EmailNotifier*** и ***SMSNotifier*** определяют интерфейсы для отправки уведомлений по электронной почте и по SMS соответственно. Класс ***User*** представляет пользователя с его именем, адресом электронной почты и номером телефона. Класс ***UserNotificationService*** использует принцип разделения интерфейса, так как клиенты этого класса зависят только от интерфейсов ***EmailNotifier*** и ***SMSNotifier***, а не от конкретных реализаций. Таким образом, можно легко добавлять новые уведомления, реализуя соответствующие интерфейсы, без внесения изменений в существующий код.



___
# 5) Принцип инверсии зависимостей (Dependency Inversion Principle)
## Зависимости должны строиться относительно абстракций, а не от конкретных реализаций.

```python
# Пример: Простая система репозитория для работы с базой данных

from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class UserRepository:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def get_user(self, user_id):
        self.database_connection.connect()
        # Логика получения пользователя из базы данных
        self.database_connection.disconnect()


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgreSQL database")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database")


class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database")

    def disconnect(self):
        print("Disconnecting from MySQL database")


# Использование кода

postgres_connection = PostgreSQLConnection()
user_repository1 = UserRepository(postgres_connection)
user_repository1.get_user(1)

mysql_connection = MySQLConnection()
user_repository2 = UserRepository(mysql_connection)
user_repository2.get_user(2)
```

В этом примере классы ***PostgreSQLConnection*** и ***MySQLConnection*** представляют конкретные реализации подключения к базе данных PostgreSQL и MySQL соответственно. Класс ***UserRepository*** реализует принцип инверсии зависимостей, так как он зависит от абстракции ***DatabaseConnection***, а не от конкретных реализаций. Это позволяет легко заменять и добавлять новые типы баз данных, расширяя класс ***UserRepository***, не изменяя его существующий код.
