from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
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
            }, status=status.HTTP_201_CREATED)
            
            # JWT token method
            # refresh = RefreshToken.for_user(users)
            # return Response({
            #     'user': serializer.data,
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # })
            
            
                    # ALT token method to use // it involves the data {} and models.py
            # data['response'] = "Registration Succesful"
            # data['username'] = users.username
            # data['email'] = users.email
            
            # token = Token.objects.get(user=users).key
            # data['token'] = token         
            # return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    