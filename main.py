def get_user(user_id: int):
    """Get user by ID."""
    return {"id": user_id}

def create_user(name: str, email: str):
    """Create a new user."""
    return {"name": name, "email": email}

class UserService:
    """Service for managing users."""

    def __init__(self, db):
        self.db = db

    def find_by_email(self, email: str):
        """Find user by email address."""
        return self.db.query(email)
