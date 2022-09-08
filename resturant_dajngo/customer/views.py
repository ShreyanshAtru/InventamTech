from rest_framework import generics
from rest_framework.response import Response
from .serializer import RegisterSerializer, ResturantSerializer, UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from .models import User, Restaurant
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



def home_page(request,id):
    obj = User.objects.get(pk=id)
    if obj.is_staff:
        """
        If user is staff(owner) or superuser , will redirect to
        admin page
        """
        return redirect('/admin/customer/restaurant')
    else:
        """
        this user is a customer , so showing the resturant deatials
        """
        resturant_obj = Restaurant.objects.all()
        return render(request, 'home.html', {'resturant_obj':resturant_obj})


#Signup 
def signup(request):
    import pdb
    pdb.set_trace()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            new_user = User(user=user)
            new_user.save()
            messages.success(request, 'User has been registered.')
            # return redirect('login_request')
        else:
            form = SignUpForm()
    return render(request, 'home.html', {'form': form})


@api_view(['POST'])
def resturant(request):
    serializer = ResturantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

