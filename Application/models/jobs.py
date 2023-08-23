"""This class represents the Job model."""
from .extensions import db
from random import choice


good_responses = ["That... was alot harder than you had expected", "All in a day's work", 
"I expected nothing less from someone of your stature", "Excellent work"]

bad_responses = ["You must be overwhelmed with shame and disappointment in yourself", "And you call yourself an adventurer",
"Sigh... Maybe you'll have better luck next time", "You have to step it up, or you'll have to rethink your career"]

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    tier = db.Column(db.Integer)

    def get_response(self) -> dict:
        """Decides whether the player passes or fails, and returns a response."""
        score = choice(list(range(10)))
        if score < 3:
            return {
                "DESCRIPTION": self.description,
                "STATUS": "failed",
                "RESPONSE": choice(bad_responses)
            }
        
        return {"DESCRIPTION": self.description, "STATUS": "passed", "RESPONSE": choice(good_responses)}
