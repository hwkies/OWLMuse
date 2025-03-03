"use client";

import * as React from 'react';
import Link from 'next/link';
import useAuth from '../../hooks/useAuth';
import CustomInput from '@/components/ui/custom-input';

/**
 * Renders a login form with username and password inputs, password visibility toggle,
 * error handling, and a link to the signup page.
 */
const SignUp = () => {
  const {
    username,
    email,
    password,
    passwordConfirmation,
    showPassword,
    err,
    handleSubmit,
    handleInputChange,
    togglePasswordVisibility,
  } = useAuth('signup');

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h2 className="text-2xl">Welcome to OWLMuse!</h2>
      <h3>Please sign up to continue.</h3>
      {err && <p className="text-red-500">{err}</p>}
      <form className="flex flex-col items-left" onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username</label>
          <CustomInput
            type="text"
            id="username"
            value={username}
            onChange={e => handleInputChange(e, 'username')}
            required
            className="rounded-xl"
          />
        </div>
        <div>
          <label htmlFor="email">Email</label>
          <CustomInput
            type="email"
            id="email"
            value={email}
            onChange={e => handleInputChange(e, 'email')}
            required
            className="rounded-xl"
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <CustomInput
            type={showPassword ? 'text' : 'password'}
            id="password"
            value={password}
            onChange={e => handleInputChange(e, 'password')}
            required
            className="rounded-xl"
          />
        </div>
        <div>
          <label htmlFor="confirmPassword">Confirm Password</label>
          <CustomInput
            type={showPassword ? 'text' : 'password'}
            id="confirmPassword"
            value={passwordConfirmation}
            onChange={e => handleInputChange(e, 'confirmPassword')}
            required
            className="rounded-xl"
          />
        </div>
        <div className="flex flex-col items-center">
          <div>
            <label htmlFor='showPasswordToggle'>{showPassword ? "Hide Password" : "Show Password"}</label>
            <input id='showPasswordToggle' type='checkbox' onClick={togglePasswordVisibility} className="ml-2" />
          </div>
          <button type="submit" className="text-xl border-2 rounded-lg px-2">
            Sign Up
          </button>
        </div>
      </form>
      <div>
        <span>Have an account? </span>
        <Link href="/login" className="text-blue-700 dark:text-blue-300">Login here.</Link>
      </div>
    </div>
  );
};

export default SignUp;