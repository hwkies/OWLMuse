"use client";
import { useState } from 'react';

const useAuth = (authType: 'login' | 'signup') => {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [passwordConfirmation, setPasswordConfirmation] = useState<string>('');
    const [showPassword, setShowPassword] = useState(false);
    const [err, setErr] = useState<string>('');
  
    /**
     * Toggles the visibility of the password input field.
     */
    const togglePasswordVisibility = () => {
      // TODO - Task 1: Toggle password visibility
      setShowPassword(!showPassword);
    };
  
    /**
     * Handles changes in input fields and updates the corresponding state.
     *
     * @param e - The input change event.
     * @param field - The field being updated ('username', 'password', or 'confirmPassword').
     */
    const handleInputChange = (
      e: ChangeEvent<HTMLInputElement>,
      field: 'username' | 'password' | 'confirmPassword',
    ) => {
      // TODO - Task 1: Handle input changes for the fields
      const { value } = e.target;
      if (field === 'username') {
        setUsername(value);
      } else if (field === 'password') {
        setPassword(value);
      } else if (field === 'confirmPassword') {
        setPasswordConfirmation(value);
      }
    };
  
    /**
     * Validates the input fields for the form.
     * Ensures required fields are filled and passwords match (for signup).
     *
     * @returns {boolean} True if inputs are valid, false otherwise.
     */
    const validateInputs = (): boolean => {
      // TODO - Task 1: Validate inputs for login and signup forms
      // Display any errors to the user
      if (
        username === null ||
        username === undefined ||
        username === '' ||
        password === null ||
        password === undefined ||
        password === ''
      ) {
        setErr('Please fill in all fields.');
        return false;
      }
      if (authType === 'signup' && password !== passwordConfirmation) {
        setErr('Passwords do not match.');
        return false;
      }
      return true;
    };
  
    /**
     * Handles the submission of the form.
     * Validates input, performs login/signup, and navigates to the home page on success.
     *
     * @param event - The form submission event.
     */
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();
  
      // TODO - Task 1: Validate inputs
  
      if (!validateInputs()) {
        return;
      }
  
      let user: User;
  
      try {
        // TODO - Task 1: Handle the form submission, calling appropriate API routes
        // based on the auth type
        if (authType === 'login') {
          user = await loginUser({ username, password });
        } else if (authType === 'signup') {
          user = await createUser({ username, password });
        } else {
          throw new Error('Invalid authentication type.');
        }
      } catch (error) {
        // TODO - Task 1: Display error message
        setErr(`Error authenticating user. ${error}`);
      }
    };
  
    return {
      username,
      password,
      passwordConfirmation,
      showPassword,
      err,
      handleInputChange,
      handleSubmit,
      togglePasswordVisibility,
    };
  };
  
  export default useAuth;