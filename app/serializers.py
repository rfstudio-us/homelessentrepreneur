from rest_framework import serializers
from .models import UserProfile
from .models import Facilities,short_survey_form,Job
from django.contrib.auth.models import User
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',]
class FacilitiesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = [
            'id',
            'name',
            'availabale_on',
            'from_time',
            'to_time',
            'owner',
            'updated_on',
            'available_date',
            'added_by',
            'facility_type',
            'geom',]
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'email',
            'mobile_no',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'qualification',
            'points_earned',
            'description',
            'city',
            'user_type',
            'cnic',
            'maritial_status',
            'technicalskills',
            'working',
            'earning',
            'medical_condition',
            'physical_condition',
            'source_earning',
            'criminal_record',
            'supported_by',
            'organization',
            'image',
            'geom',]


class ShortSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = short_survey_form
        fields = [
            'id',
            'Name',
            'Picture',
            'CNIC_Number',
            'Age',
            'Mobile_Number',]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'job_title',
            'time_stamp',
            'job_disc',
            'pay',
            'req_skill',
            'homeless_ID',
            'donot_ID',
            'geom',]
