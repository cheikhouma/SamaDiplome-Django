from django.shortcuts import render
from django import views
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializers import FeedbackSerializer
from .models import Feedback
from django.http import HttpResponse

class FeedbackView(views.View):
    def get(self, request, username=None, **kwargs):
        if username:
            user = User.objects.get(username=username)
            name = user.first_name + " " + user.last_name
            email = user.email
            return render(request, "feedbacks/feedbacks.html", {"username": username, "name": name, "email": email})
        return render(request, "feedbacks/feedbacks.html")

    def post(self, request, username=None, **kwargs):
        if username == None:
            return HttpResponse("No username, nothong to be done!")
        user = User.objects.get(username=username)
        company = request.POST.get("company")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(company=company, message=message, user=user)
        feedback.save()
        return HttpResponse("Your data stores succesfully! Do not worry, we are not going to sell them.")


class FeedbackService(APIView):
    def get(self, request, *args, **kwargs):
        """ Handles feedback retrieval requests stored """
        id = kwargs.get('id', -1)  # we assign it -1 when no 'id' parameter is provided
        
        # Retrive a single feedback if a an id is provided
        if(id != -1):
            try:
                feedback = Feedback.objects.get(id=id)
                serializer = FeedbackSerializer(feedback)
                return Response(serializer.data)
            except Feedback.DoesNotExist:
                raise NotFound(detail="Feedback requested is not found")
        # Retrive all the feedbacks otherwise
        else:
            feedbacks = Feedback.objects.all()
            serializer = FeedbackSerializer(feedbacks, many=True)
            return Response(serializer.data)

    def post(self, request):
        """ Saves a feeback informations into the database in the database """
        serializer = FeedbackSerializer(data=request.data)

        # Validate the data received
        if serializer.is_valid():  # Everything is nice
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return an error if something is wrong with the received informations
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
