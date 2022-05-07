import React, { createContext, useContext, useEffect, useState } from 'react';

export interface SignInCredentials {
  telephone: string;
  password: string;
}

interface AuthContextData {
  user: string | Record<any, string>;
  token: string;
  signIn(credentials: SignInCredentials): Promise<void>;
  signOut(): void;
  loading: boolean;
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData);

export const AuthProvider: React.FC = ({ children }) => {
  const [data, setData] = useState({ token: '' });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadStorageData();
  }, []);
  return (
    <AuthContext.Provider value={{ loading }}>{children}</AuthContext.Provider>
  );
};

export function useAuth(): AuthContextData {
  const context = useContext(AuthContext);
  return context;
}
