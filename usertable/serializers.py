from django.contrib.auth.models import User, Group
from rest_framework import serializers
from usertable.models import User as Usr
from usertable.models import Habit as Hab

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usr
        fields = ('uid','name','when_registered')


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hab
        fields = ('usr_id', 'time' , 'choice')
