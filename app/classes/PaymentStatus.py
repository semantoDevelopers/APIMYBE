from enum import Enum

class PaymentStatus(Enum):
    PENDING = 0
    COMPLETED = 1
    ERROR = 2