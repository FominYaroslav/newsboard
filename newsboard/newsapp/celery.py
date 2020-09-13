from django_celery_beat.models import PeriodicTask, IntervalSchedule

schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)
task = print("It works\n")
my_task = PeriodicTask.objects.create(interval=schedule, name='Importing contacts', task='task')

