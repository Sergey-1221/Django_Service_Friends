from rest_framework import serializers
from .models import Friend, Friend_request
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class FriendSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='second_user_id', read_only=True)
    user_name = serializers.CharField(source='second_user_name', read_only=True)

    class Meta:
        model = Friend
        fields = ('user_id', 'user_name')


class FriendSenderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='sender_id', read_only=True)
    user_name = serializers.CharField(source='sender_name', read_only=True)

    class Meta:
        model = Friend_request
        fields = ('user_id', 'user_name')

class FriendRecipientSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='recipient_id', read_only=True)
    user_name = serializers.CharField(source='recipient_name', read_only=True)

    class Meta:
        model = Friend_request
        fields = ('user_id', 'user_name')

        
'''
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''