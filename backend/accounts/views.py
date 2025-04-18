from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import Customer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

# Serve React frontend
def index(request):
    return render(request, 'index.html')

# --- SIGN UP ---
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({'message': 'All fields are required!'}, status=status.HTTP_400_BAD_REQUEST)

    if Customer.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists!'}, status=status.HTTP_400_BAD_REQUEST)

    if Customer.objects.filter(email=email).exists():
        return Response({'message': 'Email already exists!'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Create and save new customer
        customer = Customer.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return Response({'message': f'User {username} signed up successfully!'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --- SIGN IN ---
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'message': 'Username and password are required!'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)
