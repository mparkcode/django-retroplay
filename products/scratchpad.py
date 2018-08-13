from .models import Game
Game.objects.all().delete()
# Game.objects.filter(image="https://www.consolemad.co.uk/wp-content/uploads/2018/07/James-Bond-007-–-Agent-Under-Fire-250x322.jpg").delete()