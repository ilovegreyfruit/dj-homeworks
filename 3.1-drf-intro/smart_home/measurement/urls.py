from django.urls import path

from .views import SensorListCreateView, SensorRetrieveUpdateAPIView, MeasurementCreateView
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('api/sensors', SensorListCreateView.as_view(), name='sensor-list-create' ),
    path('api/sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor-detail-update' ),
    path('api/measurements/', MeasurementCreateView.as_view(), name='measurement-create' ),
]
