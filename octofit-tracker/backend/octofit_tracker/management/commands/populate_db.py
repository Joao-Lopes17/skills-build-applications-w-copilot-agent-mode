from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Captain Marvel', email='captainmarvel@marvel.com', team=marvel),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name='Pushups', description='Upper body workout'),
            Workout(name='Running', description='Cardio workout'),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        activities = [
            Activity(user=users[0], workout=workouts[0], duration=30),
            Activity(user=users[1], workout=workouts[1], duration=45),
            Activity(user=users[3], workout=workouts[0], duration=20),
        ]
        for activity in activities:
            activity.save()

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
