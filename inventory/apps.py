from django.apps import AppConfig
from django.contrib.auth import get_user_model


class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

def sayhi(self):
    print("Say hello")

def ready(self):
    User = get_user_model()
    User.sayhi = self.sayhi