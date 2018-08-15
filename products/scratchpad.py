from .models import Game, Console
console_name = Console.objects.get(console_type="mega-cd")
# console_name = Console.objects.get(console_type="master-system")
# print(console_name)
Game.objects.filter(console=console_name).delete()

# Game.objects.filter(image="https://www.consolemad.co.uk/wp-content/uploads/2018/07/James-Bond-007-–-Agent-Under-Fire-250x322.jpg").delete()