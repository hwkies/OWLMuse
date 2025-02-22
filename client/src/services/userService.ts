import axios from 'axios';
import { UserPublic } from '../types';

const USER_API_URL = `${process.env.REACT_APP_SERVER_URL}/user`;

const getUserByUsername = async (username: string): Promise<UserPublic> => {
  const res = await axios.get(`${USER_API_URL}/get_user/${username}`);
  if (res.status !== 200) {
    throw new Error('Error when fetching users');
  }
  return res.data;
};

const createUser = async (userData: { username: string; email: string; password: string }): Promise<UserPublic> => {
  try {
    const res = await axios.post(`${USER_API_URL}/create_user`, userData);
    return res.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(`Error while signing up: ${error.response.data}`);
    } else {
      throw new Error('Error while signing up');
    }
  }
};

const loginUser = async (userData: { username: string; password: string }): Promise<UserPublic> => {
  try {
    const res = await axios.post(`${USER_API_URL}/login`, userData);
    return res.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(`Error while logging in: ${error.response.data}`);
    } else {
      throw new Error('Error while logging in');
    }
  }
};

const deleteUser = async (username: string): Promise<UserPublic> => {
  const res = await axios.delete(`${USER_API_URL}/delete_user/${username}`);
  if (res.status !== 200) {
    throw new Error('Error when deleting user');
  }
  return res.data;
};

const resetPassword = async (username: string, password: string): Promise<UserPublic> => {
  const res = await axios.patch(`${USER_API_URL}/update_user`, { username, password });
  if (res.status !== 200) {
    throw new Error('Error when resetting password');
  }
  return res.data;
};

const updateEmail = async (username: string, email: string): Promise<UserPublic> => {
  const res = await axios.patch(`${USER_API_URL}/update_user`, { username, email });
  if (res.status !== 200) {
    throw new Error('Error when updating email');
  }
  return res.data;
};

export {
  getUserByUsername,
  loginUser,
  createUser,
  deleteUser,
  resetPassword,
  updateEmail,
};
