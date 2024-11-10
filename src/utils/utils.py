import random
import string


class UserUtils:
    @staticmethod
    def generate_random_username(length=8):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
