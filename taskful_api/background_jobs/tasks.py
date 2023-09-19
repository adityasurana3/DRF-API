from background_task import background
from background_task.tasks import Task as BT
from house.models import House
from task.models import COMPLETE

@background(schedule=10)
def calculate_house_stats():
    pass