from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user = User.objects.create(name='Test User', email='test@user.com', team=marvel)
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        activity = Activity.objects.create(user=user, workout=workout, duration=30)
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
