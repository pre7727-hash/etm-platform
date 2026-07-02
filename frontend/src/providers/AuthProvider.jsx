import { createContext, useEffect, useMemo, useState } from 'react';
import { supabase } from '../lib/supabaseClient';
import { attachAccessToken } from '../lib/apiClient';

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [session, setSession] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    attachAccessToken(async () => {
      const { data } = await supabase.auth.getSession();
      return data.session?.access_token;
    });
    supabase.auth.getSession().then(({ data }) => { setSession(data.session); setIsLoading(false); });
    const { data: listener } = supabase.auth.onAuthStateChange((_event, nextSession) => { setSession(nextSession); setIsLoading(false); });
    return () => listener.subscription.unsubscribe();
  }, []);

  const value = useMemo(() => ({ session, user: session?.user || null, isAuthenticated: Boolean(session?.user), isLoading, signOut: () => supabase.auth.signOut() }), [session, isLoading]);
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
