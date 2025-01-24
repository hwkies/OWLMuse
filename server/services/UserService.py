from pymssql import Cursor
#from server.db.models import User

class UserService:
    def __init__(self) -> None:
        pass

    def __user_by_username(self, username: str):
        pass


    def get_user(self, username: str):
        """
        Get a user by their username.

        Args:
            username (str): The username of the user to get.
        
        Returns:
            SafeUser: The user object with the password removed.
        """
        pass


    def create_user(self, username: str, email: str, password: str):
        """
        Create a new user with the given username, email, and password.

        Args:
            username (str): The username of the new user.
            email (str): The email of the new user.
            password (str): The password of the new user.
        
        Returns:
            SafeUser: The created user object with the password and creation date removed.
        """
        pass
        

    def login(self, username: str, password: str):
        """
        Log in a user with the given username and password.

        Args:
            username (str): The username of the user to log in.
            password (str): The password of the user to log in.
        
        Returns:
            SafeUser: The logged in user object with the password and creation date removed.
        """
        pass
        

    def update_user(self):
        """
        Update a users email or password.

        Args:
            partial (PartialUser): A partial user with the updated email, password, or both.

        Returns:
            SafeUser: The updated user object with the password and creation date removed.
        """
        pass
