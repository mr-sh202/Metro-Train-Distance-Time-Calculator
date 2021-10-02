from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta

class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Initialise the finish time to one hour from now
    self.finish_time.date = datetime.now() + timedelta(hours=1)
    # Load the available recipes from the Data Tables
    self.recipes.items = [(r['name'], r) for r in app_tables.recipes.search()]
    

  def recipes_change(self, **event_args):
    """Recalculate the schedule when choosing a new recipe"""
    self.recipe = self.recipes.selected_value
    self.update_schedule()

  def finish_time_change(self, **event_args):
    """Recalculate the schedule when choosing a new finish time"""
    self.update_schedule()
    
  def update_schedule(self):
    """Calculate the required schedule, based on the current
       recipe and the required finish time"""
    
    if self.recipe is None or self.finish_time.date is None:
      return
    
    # Keep a dict of task -> latest_start_time
    latest_starts = {}
    
    # Recursively walk the tasks in the selected recipe, calculating the latest time each can start
    def walk(task, latest_start):
      
      this_task_latest_start = latest_start - timedelta(minutes=task['duration_mins'])
      latest_starts[task] = min(this_task_latest_start, latest_starts.get(task, this_task_latest_start))
      
      for t in task['depends_on'] or []:
        walk(t, latest_starts[task])
        
    walk(self.recipe['final_task'], self.finish_time.date)
    
    task_times = latest_starts.items()
    
    # Sort the tasks by latest start time.
    task_times.sort(key=lambda t: t[1])
    
    # Display the calculated schedule.
    self.schedule_title.text = "%s Schedule" % self.recipe['name']
    self.tasks_panel.items = task_times
    self.finish_label.text = "Finish: %s" % self.finish_time.date.strftime("%H:%M")



