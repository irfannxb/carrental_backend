from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 🔥 Add custom claims to the token payload
        token['user_id'] = user.id
        token['email'] = user.email
        token['username'] = user.username

        return token

    def validate(self, attrs):
        # Call parent validate to get the default response (access, refresh tokens)
        data = super().validate(attrs)

        # Add user information to the response
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        # data['email'] = self.user.email
        # data['username'] = self.user.username

        return data
