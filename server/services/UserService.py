from pymssql import Cursor
from server.models.User import SafeUser, PartialUser

class UserService:
    def __init__(self, cursor: Cursor) -> None:
        self.cursor = cursor

    def __user_by_username(self, username: str) -> SafeUser:
        query = f'SELECT username, email, created_at FROM dbo.Users WHERE username = %s'
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        if user is None:
            return None
        return { 'username': user['Username'], 'email': user['Email'], 'created_at': user['CreatedAt'] }


    def get_user(self, username: str) -> SafeUser:
        """
        Get a user by their username.

        Args:
            username (str): The username of the user to get.
        
        Returns:
            SafeUser: The user object with the password removed.
        """
        user = self.__user_by_username(username)
        if user is None:
            raise Exception('User not found')
        return { 'username': user['Username'], 'email': user['Email'], 'created_at': user['CreatedAt'] }


    def create_user(self, username: str, email: str, password: str) -> SafeUser:
        """
        Create a new user with the given username, email, and password.

        Args:
            username (str): The username of the new user.
            email (str): The email of the new user.
            password (str): The password of the new user.
        
        Returns:
            SafeUser: The created user object with the password and creation date removed.
        """
        user = self.__user_by_username(username)
        if user is not None:
            raise Exception('A User with that username already exists!')
        insert_query = f'INSERT INTO dbo.Users (username, email, password) VALUES (%s, %s, %s)'
        self.cursor.execute(insert_query, (username, email, password))
        self.cursor.connection.commit()
        return { 'username': username, 'email': email }
        

    def login(self, username: str, password: str) -> SafeUser:
        """
        Log in a user with the given username and password.

        Args:
            username (str): The username of the user to log in.
            password (str): The password of the user to log in.
        
        Returns:
            SafeUser: The logged in user object with the password and creation date removed.
        """
        query = f'SELECT username, email FROM dbo.Users WHERE username = %s AND password = %s'
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        if user is None:
            raise Exception('Invalid username or password.')
        return { 'username': user['Username'], 'email': user['Email'] }
        

    def update_user(self, partial: PartialUser) -> SafeUser:
        """
        Update a users email or password.

        Args:
            partial (PartialUser): A partial user with the updated email, password, or both.

        Returns:
            SafeUser: The updated user object with the password and creation date removed.
        """
        # Determine if the user exists, if they do get their email
        user = self.__user_by_username(partial['username'])
        if user is None:
            raise Exception('User not found!')
        else:
            email = user['email']
        # Determine which fields need to be updated
        update_email = partial.get('email') is not None
        update_password = partial.get('password') is not None
        # Update the fields specified to be updated
        if not update_email and not update_password:
            raise Exception('No fields to update.')
        if update_email and update_password:
            query = f'UPDATE dbo.Users SET email = %s, password = %s WHERE username = %s'
            params = (partial['email'], partial['password'], partial['username'])
            updated = { 'username': partial['username'], 'email': partial['email'] }
        elif update_email:
            query = f'UPDATE dbo.Users SET email = %s WHERE username = %s'
            params = (partial['email'], partial['username'])
            updated = { 'username': partial['username'], 'email': partial['email'] }
        else:
            query = f'UPDATE dbo.Users SET password = %s WHERE username = %s'
            params = (partial['password'], partial['username'])
            updated = { 'username': partial['username'], 'email': email }
        self.cursor.execute(query, params)
        self.cursor.connection.commit()
        return updated
