# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Facilities,UserProfile,Job,short_survey_form
from .serializers import FacilitiesDetailSerializer,UserProfileSerializer,JobSerializer,ShortSurveySerializer,UserDetailSerializer

from django.http import Http404
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView, 
)

from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


class JobList(APIView):
    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        snippets = Job.objects.all()
        null = None
        snippets = snippets.filter(homeless_ID=null)
        serializer = JobSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortSurveyList(APIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        snippets = short_survey_form.objects.all()
        null = None
        snippets = snippets.filter(homeless_ID=null)
        serializer = ShortSurveySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShortSurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profile_API(APIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
       try:
           return UserProfile.objects.get(pk=pk)
       except UserProfile.DoesNotExist:
           raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserProfileSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserProfileSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Facility_API(APIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
       try:
           return Facilities.objects.get(pk=pk)
       except Facilities.DoesNotExist:
           raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FacilitiesDetailSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FacilitiesDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacilitiesList(APIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        snippets = Facilities.objects.all()
        null = None
        snippets = snippets.filter(homeless_ID=null)
        serializer = FacilitiesDetailSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FacilitiesDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def facility_view(request):
    js=serialize('geojson', Facilities.objects.all(),geometry_field='geom', fields=('name','facility_type','added_by'))
    return render(request, 'map.html',{'data':js})


class All_Facilities_API(ListAPIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = FacilitiesDetailSerializer
    def get_queryset(self):
        queryset = Facilities.objects.all()
        fac_type = self.request.query_params.get('fac_type', None)
        if fac_type is not None:
            queryset = queryset.filter(facility_type=fac_type)
        return queryset


class get_user_profile(ListAPIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    def get_queryset(self):

        queryset = UserProfile.objects.all()
        user_id = self.request.query_params.get('userid', None)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset
class get_user_details(ListAPIView):

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer
    model = User
    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.query_params.get('userid', None)
        if user_id is not None:
            queryset = queryset.filter(id=user_id)
        return queryset
@login_required


@login_required
def all_data(request):
    qs = Facilities.objects.all()
    js_water=serialize('geojson', Facilities.objects.filter(facility_type='Water'),geometry_field='geom')
    js_education=serialize('geojson', Facilities.objects.filter(facility_type='Education'),geometry_field='geom')
    js_health=serialize('geojson', Facilities.objects.filter(facility_type='Health'),geometry_field='geom')
    js_shelter=serialize('geojson', Facilities.objects.filter(facility_type='Shelter homes'),geometry_field='geom')
    js_homeless=serialize('geojson', UserProfile.objects.filter(user_type='homeless'),geometry_field='geom')
    js_donor=serialize('geojson', UserProfile.objects.filter(user_type='donor'),geometry_field='geom')
    return render(request, 'map.html',{'water_data':js_water,'education_data':js_education,'health_data':js_health,'shelter_data':js_shelter,
                                        'homeless_data':js_homeless,'donor_data':js_donor})

class All_user_API(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class All_homeless_API(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.filter(user_type='homeless')
    serializer_class = UserProfileSerializer
#class All_donor_API(ListAPIView):
#    queryset = UserProfile.objects.filter(user_type='donor')
#    serializer_class = UserProfileSerializer













