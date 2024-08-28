from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.api.serializers import registrationSerializer
# from user_app import models

@api_view(['POST',])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)       

@api_view(['POST', ])
def registration_view(request):
     
    if request.method == 'POST':
        serializer = registrationSerializer(data=request.data)
        
        # data = {}
               
        if serializer.is_valid():
            users = serializer.save()  
            # Create a token for the new user
            token, created = Token.objects.get_or_create(user=users)
            return Response({
                'token': token.key,
                'user': serializer.data
            })
                    # ALT token method to use // it involves the data {} and models.py
            # data['response'] = "Registration Succesful"
            # data['username'] = users.username
            # data['email'] = users.email
            
            # token = Token.objects.get(user=users).key
            # data['token'] = token         
            # return Response(data)
            
        return Response(serializer.errors)
    