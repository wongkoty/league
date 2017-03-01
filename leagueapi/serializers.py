from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Champion

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField('get_links')

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active',)

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',
                kwargs={user.USERNAME_FIELD: username}, request=request)
        }


class ChampionSerializer(serializers.ModelSerializer):

    # links = serializers.SerializerMethodField('get_links')

    class Meta:
        model = Champion
        fields = ('id', 'name', 'description', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('champion-detail',
                kwargs={'pk': obj.pk}, request=request),
        }

