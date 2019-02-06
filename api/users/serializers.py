from rest_framework.serializers import (
    CharField,EmailField,
    ModelSerializer,ValidationError
)
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class UserSerializer(ModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":{
                "write_only": True
            }
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        validated_data['token'] = token
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    username = CharField(required=False,allow_blank=True)
    email = EmailField(label='Email address',required=False,allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":{
                "write_only": True
            }
        }
        
    def validate(self, data):
        email=data.get("email",None)
        username = data.get("username",None)
        password = data["password"]
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            if user.is_active:

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                data['token'] = token
                return data
            else:
                raise ValidationError('Your account has been disabled.')
        else:
            raise ValidationError('Incorrect Credentials.')
        return data