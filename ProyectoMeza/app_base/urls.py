from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio_vista, name='inicio'),
    path('agendar-cita/', views.agendarCita, name='agendarCita'),
    path('citas-agendadas/', views.citasAgendadas, name='citasAgendadas'),
    path('seleccionarPaciente/<int:id_paciente>/', views.seleccionarPaciente, name='seleccionarPaciente'),
    path('borrarPaciente/<int:id_paciente>/', views.borrarPaciente, name='borrarPaciente'),
    path('actualizarPaciente/<int:id_paciente>/', views.actualizarPaciente, name='actualizarPaciente'),
]
urlpatterns += static('/images/', document_root='images')
