from django.urls import path
from forms_app.views import contatti, registrazioneView

app_name = "forms_app"

urlpatterns = [
    path("contattaci/", contatti, name="contatti"),
    path("registrazione/", registrazioneView, name="registrati")
]
