from model import User;

def get_user(user_id):
    # Simulating fetching user data from a database or an API
    if user_id == 1:
        return User(id=1, name="Kishor Patidar", age=29, skills=["Python", "JavaScript", "Machine Learning"])
    else:
        return None
    