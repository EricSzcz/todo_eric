# from django.db import models
# from django.contrib.auth.models import User
# from django.dispatch import receiver
#
# class Usuario(models.Model):
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#
# @receiver(post_save, sender=User)
# def criar_perfil(sender, instance, created, **kwargs):
#     if created:
#         Usuario.objects.create(user=instance)
#
# @receiver(post_save, sender=User):
# def salvar_perfil(sender, instance, **kwargs):
#     instance.Usuario.save()