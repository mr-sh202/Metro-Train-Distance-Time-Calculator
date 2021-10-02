import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )
  
  anvil.email.send(#to="noreply@anvil.works", # Messages go to the app owner by default. Uncomment and modify to send the email elsewhere
                   subject="Feedback from {}".format(name),
                   text=f"""
A new person has filled out the feedback form!

Name: {name}
Email address: {email}
Feedback:
{feedback}
""")

#