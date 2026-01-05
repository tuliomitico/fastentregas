import React, {
  createContext,
  useState,
  useEffect,
  useContext,
  useCallback,
} from 'react';
import { useRouter } from 'next/navigation';
import Cookies from 'universal-cookie';

import api from '@fastentregas/axios-config';
import AuthService from '../services/AuthService';

type User = {
  name: string;
  telephone: string;
};

type SignInData = {
  telephone: string;
  password: string;
};

type AuthContextType = {
  isAuthenticated: boolean;
  user: User;
  signIn: (data: SignInData) => Promise<void>;
  signOut: () => void;
};

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const router = useRouter();
  const cookie = new Cookies();
  const isAuthenticated = !!user;

  useEffect(() => {
    const token = cookie.get('nextauth.token');
  }, []);

  const signIn = useCallback(async ({ telephone, password }: SignInData) => {
    const {
      data: { token, user },
    } = await AuthService.signIn({ telephone, password });

    cookie.set('nextauth.token', token, {
      maxAge: 60 * 60 * 1, // 1 hour
    });

    api.defaults.headers.authorization = `Bearer ${token}`;

    setUser(user);
    router.push('/dashboard');
  }, []);

  const signOut = useCallback(async () => {
    cookie.remove('nextauth.token');
    setUser(null);
  }, []);

  return (
    <AuthContext.Provider value={{ isAuthenticated, signIn, user, signOut }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextType {
  const context = useContext(AuthContext);
  return context;
}
