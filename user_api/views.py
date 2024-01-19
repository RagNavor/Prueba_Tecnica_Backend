from django.contrib.sessions.models import Session
from rest_framework.response import Response
from .serializers import UserSerializer, UserTokenSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from datetime import datetime

# Create your views here.


class UserApi(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validate_username(request.data['email']):
                user = serializer.save()
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            return Response({'message':'Usuario ya existe'}, status=status.HTTP_409_CONFLICT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data , context = {'request':request})
        print(request.data)
        if login_serializer.is_valid(raise_exception=True):
            user = login_serializer.validated_data['user']
            if user.is_active:
                print(user)
                token,created = Token.objects.get_or_create(user = user)
                if created:
                    return Response({'token': token.key,
                                    'message': 'inicio de session completo'},
                                    status=status.HTTP_202_ACCEPTED)
                else:
                    all_session = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({'token': token.key,
                                    'message': 'inicio de session completo'},
                                    status=status.HTTP_202_ACCEPTED)
                
            else:
                return Response({'message': 'Usuario inactivo, por favor contacte al administrador'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:    
                return Response({'message': 'Nombre de usuario o contraseña incorrectos'}, 
                                status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Nombre dejhbjnkjn usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
            
class Logout(APIView):
    def get(self,request):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key=token).first()
            if token:
                user = token.user
                all_session = Session.objects.filter(expire_date__gte = datetime.now())
                if all_session.exists():
                    for session in all_session:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message= 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado'
                return Response({'token_message':token_message,'session_message':session_message})
            
        
            return Response({'error':'No se encontro el token'},status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({'error':'No se envio    un token'},status=status.HTTP_400_BAD_REQUEST)
    