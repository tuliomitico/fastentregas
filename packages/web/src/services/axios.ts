import api from '@fastentregas/axios-config';
import { cookies } from 'next/headers';

export function getAPIClient() {
  const token = cookies().get('nextauth.token')?.value ?? null;

  api.interceptors.request.use(config => {
    return config;
  });

  if (token) {
    api.defaults.headers.authorization = `Bearer ${token}`;
  }

  return api;
}
