# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from simple_history.models import HistoricalRecords

from django.contrib.gis.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length=100, default='',blank=True, null=True)
    mobile_no = models.CharField(max_length=20, default='',blank=True, null=True)
    first_name = models.CharField(max_length=100, default='',blank=True, null=True)
    last_name = models.CharField(max_length=100, default='',blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, default='',blank=True, null=True)
    qualification = models.CharField(max_length=100, default='',blank=True, null=True)
    points_earned = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default='',blank=True, null=True)
    city = models.CharField(max_length=100, default='',blank=True, null=True)
    user_type = models.CharField(max_length=50,default='',blank=True, null=True)
    cnic = models.CharField(max_length=50,default='',blank=True, null=True)
    maritial_status =models.CharField(max_length=50,default='',blank=True, null=True)
    technicalskills =models.TextField(blank=True, null=True)
    working =models.BooleanField(default=False)
    earning =models.IntegerField(default=0)
    medical_condition =models.CharField(max_length=100, default='',blank=True, null=True)
    physical_condition = models.CharField(max_length=100, default='',blank=True, null=True)
    source_earning = models.CharField(max_length=100, default='',blank=True, null=True)
    criminal_record =models.CharField(max_length=100, default='',blank=True, null=True)
    supported_by =models.CharField(max_length=100, default='',blank=True, null=True)
    organization = models.CharField(max_length=100, default='',blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



class Donations(models.Model):
    time_stamp = models.DateTimeField(blank=True, null=True)
    type_donation = models.TextField(blank=True, null=True)
    homeless_ID = models.ForeignKey(User, models.DO_NOTHING,related_name='%(class)s_donated_to')
    donot_ID = models.ForeignKey(User, models.DO_NOTHING,related_name='%(class)s_donated_by')
    recieved_by_donor=models.BooleanField(default=False)
    geom = models.PointField(blank=True, null=True)
    def __unicode__(self):
        return self.time_stamp

class Job(models.Model):
    job_title = models.TextField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    job_disc = models.TextField(blank=True, null=True)
    pay = models.IntegerField(blank=True, null=True)
    req_skill = models.TextField(blank=True, null=True)
    homeless_ID = models.IntegerField(blank=True, null=True)
    donot_ID = models.ForeignKey(User, models.DO_NOTHING,related_name='%(class)s_donated_by')
    geom = models.PointField(blank=True, null=True)
    def __unicode__(self):
        return self.job_title
class Facilities(models.Model):
    name = models.TextField(blank=True, null=True)
    availabale_on = models.TextField(blank=True, null=True)
    from_time = models.DateTimeField(blank=True, null=True)
    to_time = models.DateTimeField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    available_date=models.DateTimeField(blank=True, null=True)
    added_by =models.ForeignKey(User, models.DO_NOTHING)
    facility_type =models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class location_history (models.Model):
    time_stamp = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    geom = models.PointField()
    def __unicode__(self):
        return self.user_id.username

class survey_form(models.Model):
    Name = models.TextField(blank=True, null=True)
    Picture = models.ImageField(upload_to='survey_profile_image', blank=True, null=True)
    Gender = models.TextField(blank=True, null=True)
    Nationality = models.TextField(blank=True, null=True)
    Birth_Date = models.TextField(blank=True, null=True)
    Birth_Place = models.TextField(blank=True, null=True)
    CNIC_Number = models.TextField(blank=True, null=True)
    Age = models.IntegerField(default=0)
    Mobile_Number = models.TextField(blank=True, null=True)
    Address_Permanent = models.TextField(blank=True, null=True)
    Address_Temporary = models.TextField(blank=True, null=True)
    Reason_for_being_homeless = models.TextField(blank=True, null=True)
    Where_do_you_want_to_be_accommodated = models.TextField(blank=True, null=True)
    Address_of_your_Relatives_House = models.TextField(blank=True, null=True)
    What_kind_of_service_do_you_need = models.TextField(blank=True, null=True)
    Since_how_long_have_you_been_homeless = models.TextField(blank=True, null=True)
    Any_Criminal_Record = models.TextField(blank=True, null=True)
    If_you_are_released_from_jail_what_was_the_reason = models.TextField(blank=True, null=True)
    For_how_long_time_you_are_in_jail = models.TextField(default=0)
    Marital_Status = models.TextField(blank=True, null=True)
    Do_you_have_family = models.TextField(blank=True, null=True)
    Family_Members = models.TextField(default=0)
    Are_your_children_enrolled_in_any_school = models.TextField(blank=True, null=True)
    Do_you_need_aid_to_pay_their_fee = models.TextField(blank=True, null=True) 
    If_no_then_how_are_you_manage_educational_expenses = models.TextField(blank=True, null=True)
    Any_Disease_to_your_family_members = models.TextField(blank=True, null=True)
    Do_you_have_any_children_with_disability = models.TextField(blank=True, null=True)
    What_is_your_average_earning_on_daily_basis_rupees = models.IntegerField(default=0)
    Monthly_income = models.IntegerField(default=0)
    What_is_your_source_of_earning = models.TextField(blank=True, null=True)
    Do_you_know_how_to_read = models.TextField(blank=True, null=True) 
    Do_you_know_how_to_write = models.TextField(blank=True, null=True)
    What_is_your_education = models.TextField(blank=True, null=True)
    Do_you_have_any_technical_knowledge_skills = models.TextField(blank=True, null=True)
    Do_you_need_any_trainings_diploma_1 = models.TextField(blank=True, null=True)
    If_yes_then_specify_1 = models.TextField(blank=True, null=True)
    Can_you_afford_your_educational_expenses = models.TextField(blank=True, null=True)
    Any_support_from_parents_guardian_others = models.TextField(blank=True, null=True)
    Do_you_have_any_disease_2 = models.TextField(blank=True, null=True)
    If_yes_please_specify_2 = models.TextField(blank=True, null=True)
    For_how_long_have_you_not_visited_any_doctor = models.TextField(blank=True, null=True)
    Are_you_currently_taking_any_medication_3 = models.TextField(blank=True, null=True)
    If_yes_please_specify_3 = models.TextField(blank=True, null=True)
    How_many_hours_do_you_sleep = models.TextField(default=0)
    Are_you_able_to_eat_regularly = models.TextField(blank=True, null=True)
    How_often_do_you_eat = models.TextField(default=0)
    Did_it_affect_your_health_4 = models.TextField(blank=True, null=True)
    if_yes_then_how_4 = models.TextField(blank=True, null=True)
    How_can_we_solve_world_hunger = models.TextField(blank=True, null=True)
    Did_your_household_run_out_of_food = models.TextField(blank=True, null=True)
    Do_you_have_any_physical_disability_5 = models.TextField(blank=True, null=True)
    If_yes_then_what_sorts_of_illnesses_you_have_5 = models.TextField(blank=True, null=True)
    What_is_the_severity_level_disability_from_1_to_10 = models.IntegerField(default=0)
    What_treatments_have_been_recommended = models.TextField(blank=True, null=True)
    Disable_people_have_equal_opportunities_in_edu_6 = models.TextField(blank=True, null=True)
    If_yes_please_specify_6 = models.TextField(blank=True, null=True) 
    In_the_context_of_state_benefits_for_disable_people = models.TextField(blank=True, null=True)
    Type_of_Drug = models.TextField(blank=True, null=True)
    Have_you_ever_felt_you_should_stop_doing_the_drug = models.TextField(blank=True, null=True)
    Have_you_annoyed_when_criticized_for_using_drug = models.TextField(blank=True, null=True)
    Have_you_ever_felt_guilty_about_your_using_drug = models.TextField(blank=True, null=True)
    Have_you_take_drugs_immediately_in_the_morning = models.TextField(blank=True, null=True)
    Do_you_feel_you_must_consume_drug_to_pass_your_day_7 = models.TextField(blank=True, null=True)
    If_yes_then_why_7 = models.TextField(blank=True, null=True) 
    Have_you_seek_medical_attention_because_of_drug_use_8 = models.TextField(blank=True, null=True)
    If_yes_then_how_often_8 = models.TextField(blank=True, null=True)
    Has_your_performance_at_work_affected_by_drug_usage = models.TextField(blank=True, null=True)
    Have_you_worry_about_the_next_time_you_will_take_drug = models.TextField(blank=True, null=True)
    Has_your_drug_use_cause_issue_in_personal_relation_9 = models.TextField(blank=True, null=True)
    If_yes_then_state_what_kind_of_problems_occurred_9 = models.TextField(blank=True, null=True)
    Have_you_suffered_from_memory_loss_after_using_drugs = models.TextField(blank=True, null=True)
    Do_you_experience_symptoms_after_not_consuming_drugs = models.TextField(blank=True, null=True)
    Do_you_go_to_extensive_lengths_to_obtain_drugs = models.TextField(blank=True, null=True)
    Do_you_remain_intoxicated_for_several_days_at_a_time = models.TextField(blank=True, null=True)
    Have_you_do_things_while_intoxicate_and_later_regret = models.TextField(blank=True, null=True)
    What_is_the_hardest_part_about_being_homeless = models.TextField(blank=True, null=True)
    Would_you_like_to_change_your_situation_10 = models.TextField(blank=True, null=True)
    If_yes_then_how_10 = models.TextField(blank=True, null=True)
    Do_you_think_it_possible_to_change_your_situation = models.TextField(blank=True, null=True)
    What_do_you_expect_from_us = models.TextField(blank=True, null=True)
    If_we_help_you_then_what_to_do_in_return_as_favor = models.TextField(blank=True, null=True)
    What_have_you_done_to_revert_your_condition = models.TextField(blank=True, null=True)
    taken_at = models.DateTimeField(blank=True, null=True)
    Survey_taken_by = models.ForeignKey(User, models.DO_NOTHING)
    geom = models.PointField(blank=True, null=True)
    def __unicode__(self):
       return self.Name

class short_survey_form(models.Model):
    Name = models.TextField(blank=True, null=True)
    Picture = models.ImageField(upload_to='survey_profile_image', blank=True, null=True)
    CNIC_Number = models.TextField(blank=True, null=True)
    Age = models.IntegerField(default=0)
    Mobile_Number = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.Name
