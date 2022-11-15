from rest_framework import routers

from games.views import GameViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("game", GameViewSet)
