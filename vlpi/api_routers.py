from rest_framework.routers import DefaultRouter
from etalons import views as etalons_views
from modules import views as modules_views
from tasks import views as tasks_views
from users import views as users_views


router = DefaultRouter()
router.register("etalons", etalons_views.EtalonViewSet)
router.register("modules", modules_views.StudyingModuleViewSet)
router.register("tasks", tasks_views.TaskViewSet)
router.register("tasks_progresses", tasks_views.UserTaskProgressViewSet)
router.register("users", users_views.UserViewSet)

urlpatterns = []
urlpatterns = router.urls

app_name = "api"
