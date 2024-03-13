from django.urls import path

from modules.apps import ModulesConfig
from modules.views import ModuleUpdateAPIview, ModuleListAPIview, ModuleDestroyAPIview, ModuleRetrieveAPIview, ModuleCreateAPIview

app_name = ModulesConfig.name

urlpatterns = [
    path('module/create/', ModuleCreateAPIview.as_view(), name='create_module'),
    path('modules/', ModuleListAPIview.as_view(), name='all_modules'),
    path('module/<int:pk>/', ModuleRetrieveAPIview.as_view(), name='one_module'),
    path('module/update/<int:pk>/', ModuleUpdateAPIview.as_view(), name='update_module'),
    path('module/delete/<int:pk>/', ModuleDestroyAPIview.as_view(), name='delete_module'),
]
