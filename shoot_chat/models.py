from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    chats = models.CharField(max_length=200)
    id_rols = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    cognoms = models.CharField(max_length=200)
    correu = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
   
class Textchat(models.Model):
    id_chat = models.CharField(max_length=200)
    id_user = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)

class Chatsusuari(models.Model):
    id_usuaris = models.CharField(max_length=200)
    id_chats = models.CharField(max_length=200)

class Chat(models.Model):
    id_adminchat = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    descripcio = models.CharField(max_length=200)