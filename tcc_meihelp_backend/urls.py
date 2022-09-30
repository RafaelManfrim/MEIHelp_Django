from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from tcc_meihelp_backend.activities.API.viewsets import ActivityViewset
from tcc_meihelp_backend.companies.API.viewsets import CNPJViewset, CompanyViewset, CompanyTokenObtainPairView
from tcc_meihelp_backend.inventory.API.viewsets import InventoryViewset, ProductViewset, ProviderViewset, \
    StockProductViewset
from tcc_meihelp_backend.taxes.API.viewsets import DASViewset
from tcc_meihelp_backend.trainings.API.viewsets import TrainingViewset

router = routers.SimpleRouter()
router.register(r'cnpj', CNPJViewset, basename='CNPJ')
router.register(r'companies', CompanyViewset, basename='Company')
router.register(r'activities', ActivityViewset, basename='Activity')
router.register(r'trainings', TrainingViewset, basename='Training')
router.register(r'stocks', InventoryViewset, basename='Stock')
router.register(r'products', ProductViewset, basename='Product')
router.register(r'providers', ProviderViewset, basename='Provider')
router.register(r'stock_product', StockProductViewset, basename='StockProduct')
router.register(r'das', DASViewset, basename='DAS')
# router.register(r'dre')
# router.register(r'cashflow')
# router.register(r'reports')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/login/', CompanyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
