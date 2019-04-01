from django.db import models



# from django.contrib.auth.models import User

class State(models.Model):
    player              = models.ForeignKey(User, on_delete=models.CASCADE)
    duskball_is         = models.BooleanField()
    haunted_painting_is = models.BooleanField()
    lucario_is          = models.BooleanField()
    computer_on         = models.BooleanField()
    poke_ball_is        = models.BooleanField()
    left_corner_is      = models.BooleanField()
    right_corner_is     = models.BooleanField()
    bookshelf_is        = models.BooleanField()
    bear_is             = models.BooleanField()
    move_ball_down      = models.BooleanField()
    ball_gone           = models.BooleanField()
    scroll_is           = models.BooleanField()
    stair_collision     = models.IntegerField()
    cabnet_collision    = models.IntegerField()
    rail2_collision     = models.IntegerField()  
    duskball_collision  = models.IntegerField()
    painting_collision  = models.IntegerField()
    haunted_collision   = models.IntegerField()
    lucario_collision   = models.BooleanField()
    timestamp           = models.DateTimeField(auto_now_add=True)
