from django.contrib.auth.models import User
from rest_framework import serializers

class registrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password1' ]
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password1 = self.validated_data['password1']
        
        if password != password1:
            raise serializers.ValidationError({'error' : 'Password provided did not match'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error' : 'EmailAlready Exists!'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account