import React, {
  createContext,
  useState,
  useEffect,
  useContext,
  useCallback,
} from 'react';
import { useRouter } from 'next/navigation';
import { setCookie, destroyCookie, parseCookies } from 'nookies';

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
  const isAuthenticated = !!user;

  useEffect(() => {
    const { 'nextauth.token': token } = parseCookies();
  }, []);

  const signIn = useCallback(async ({ telephone, password }: SignInData) => {
    const {
      data: { token, user },
    } = await AuthService.signIn({ telephone, password });

    setCookie(undefined, 'nextauth.token', token, {
      maxAge: 60 * 60 * 1, // 1 hour
    });

    api.defaults.headers.authorization = `Bearer ${token}`;

    setUser(user);
    router.push('/dashboard');
  }, []);

  const signOut = useCallback(async () => {
    destroyCookie(undefined, 'nextauth.token');
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
