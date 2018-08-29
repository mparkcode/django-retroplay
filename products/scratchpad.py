from .models import Game, Console

for row in Game.objects.all():
    if Game.objects.filter(title=row.title).count() > 1:
        row.delete()