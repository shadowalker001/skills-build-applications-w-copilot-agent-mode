from django.core.management.base import BaseCommand
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

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel')

        # Create activities
        Activity.objects.create(user='Iron Man', activity_type='run', duration=30, date='2026-02-22')
        Activity.objects.create(user='Superman', activity_type='fly', duration=60, date='2026-02-22')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=100)
        Leaderboard.objects.create(team='dc', points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Flight', description='Fly for 1 hour', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
