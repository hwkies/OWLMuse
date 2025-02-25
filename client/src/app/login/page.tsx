"use client";

import * as React from 'react';
import Link from 'next/link';
import useAuth from '../../hooks/useAuth';
import CustomInput from '@/components/ui/custom-input';

/**
 * Renders a login form with username and password inputs, password visibility toggle,
 * error handling, and a link to the signup page.
 */
const Login = () => {
  const {
    username,
    password,
    showPassword,
    err,
    handleSubmit,
    handleInputChange,
    togglePasswordVisibility,
  } = useAuth('login');

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h2 className="text-2xl">Welcome to OWLMuse!</h2>
      <h3>Please login to continue.</h3>
      <form className="flex flex-col items-left">
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
      </form>
      <div className="flex flex-col items-center">
        <div>
          <label htmlFor='showPasswordToggle'>{showPassword ? "Hide Password" : "Show Password"}</label>
          <input id='showPasswordToggle' type='checkbox' value={showPassword} onClick={togglePasswordVisibility} className="ml-2" />
        </div>
        <button type="submit" className="text-xl border-2 rounded-lg px-2">
          Login
        </button>
      </div>
      <div>
        <span>Don&apos;t have an account? </span>
        <Link href="/signup" className="text-blue-700 dark:text-blue-300">Sign up here.</Link>
      </div>
    </div>
  );
};

export default Login;