from datetime import datetime
from pymssql import Cursor
from server.types import SafeUser, PartialUser

class User:
    def __init__(self, cursor: Cursor) -> None:
        self.cursor = cursor

    def create_user(self, username: str, email: str, password: str) -> SafeUser:
        try:
            user_exists_query = f'SELECT COUNT(*) FROM dbo.Users WHERE username = {username}'
            self.cursor.execute(user_exists_query)
            if self.cursor.fetchone()[0] > 0:
                return { 'error': 'User already exists' }
            insert_query = f'INSERT INTO dbo.Users (username, email, password, created_at) VALUES ({username}, {email}, {password})'
            self.cursor.execute(insert_query)
            self.cursor.connection.commit()
            return { 'username': username, 'email': email }
        except Exception:
            return {  'error': 'Error when creating a user' }
    
    def get_user(self, username: str) -> SafeUser:
        try:
            query = f'SELECT username, email, created_at FROM dbo.Users WHERE username = {username}'
            self.cursor.execute(query)
            user = self.cursor.fetchone()
            if user is None:
                return { 'error': 'User not found' }
            return { 'username': user['Username'], 'email': user['Email'], 'created_at': user['CreatedAt'] }
        except Exception:
            return {  'error': 'Error when getting a user' }
        
    def login(self, username: str, password: str) -> SafeUser:
        try:
            query = f'SELECT username, email, created_at FROM dbo.Users WHERE username = {username} AND password = {password}'
            self.cursor.execute(query)
            user = self.cursor.fetchone()
            if user is None:
                return { 'error': 'Invalid username or password' }
            return { 'username': user['Username'], 'email': user['Email'] }
        except Exception:
            return {  'error': 'Error when logging in' }
        
    def update_user(self, partial: PartialUser) -> SafeUser:
        try:
            # Determine if the user exists, if they do get their email
            user_exists_query = f'SELECT username, email, created_at FROM dbo.Users WHERE username = {partial['username']}'
            self.cursor.execute(user_exists_query)
            user = self.cursor.fetchone()
            if user is None:
                return { 'error': 'User to update not found' }
            else:
                email = user[1]
            # Determine which fields need to be updated
            update_email = partial.get('email') is not None
            update_password = partial.get('password') is not None
            # Update the fields specified to be updated
            if not update_email and not update_password:
                return { 'error': 'No fields to update' }
            if update_email and update_password:
                query = f'UPDATE dbo.Users SET email = {partial["email"]}, password = {partial["password"]} WHERE username = {partial["username"]}'
                updated = { 'username': partial['username'], 'email': partial['email'] }
            elif update_email:
                query = f'UPDATE dbo.Users SET email = {partial["email"]} WHERE username = {partial["username"]}'
                updated = { 'username': partial['username'], 'email': partial['email'] }
            else:
                query = f'UPDATE dbo.Users SET password = {partial["password"]} WHERE username = {partial["username"]}'
                self.cursor.execute(f'SELECT email FROM dbo.Users WHERE username = {partial["username"]}')
                updated = { 'username': partial['username'], 'email': email }
            self.cursor.execute(query)
            self.cursor.connection.commit()
            return updated
        except Exception:
            return {  'error': 'Error when updating a user' }
