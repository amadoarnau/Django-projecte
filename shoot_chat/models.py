from __future__ import unicode_literals
from django.db import models




class User(models.Model):
    username = models.CharField(max_length=200)
    id_rols = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    cognoms = models.CharField(max_length=200)
    correu = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Chat(models.Model):
    adminchat = models.ForeignKey(User, null='true')
    nom = models.CharField(max_length=200)
    descripcio = models.CharField(max_length=200)
    def __str__(self):
        return self.nom
   
class Textchat(models.Model):
    nomchat = models.ForeignKey(Chat, null='true')
    nomusuari = models.ForeignKey(User, null='true')
    valor = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    def __str__(self):
        return self.valor

class Chatsusuari(models.Model):
    id_usuaris = models.CharField(max_length=200)
    id_chats = models.CharField(max_length=200)
    def __str__(self):
        return self.id_usuaris

