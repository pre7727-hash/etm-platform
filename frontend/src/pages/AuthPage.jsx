import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Github, Mail } from 'lucide-react';
import { Logo } from '../components/brand/Logo.jsx';
import { Button } from '../components/ui/Button.jsx';
import { supabase } from '../lib/supabaseClient';

export function AuthPage({ mode }) {
  const isRegister = mode === 'register';
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: '', username: '', password: '' });
  const [status, setStatus] = useState({ loading: false, error: '', success: '' });

  async function handleSubmit(event) {
    event.preventDefault();
    setStatus({ loading: true, error: '', success: '' });
    const redirectTo = window.location.origin;
    const result = isRegister
      ? await supabase.auth.signUp({ email: form.email, password: form.password, options: { data: { username: form.username }, emailRedirectTo: redirectTo } })
      : await supabase.auth.signInWithPassword({ email: form.email, password: form.password });
    if (result.error) { setStatus({ loading: false, error: result.error.message, success: '' }); return; }
    setStatus({ loading: false, error: '', success: isRegister ? 'Check your inbox to confirm your account.' : 'Signed in successfully.' });
    if (!isRegister) navigate('/');
  }

  async function handleOAuth(provider) {
    await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: window.location.origin } });
  }

  return <section className="grid min-h-screen place-items-center bg-[#070c10] px-4 py-10"><div className="w-full max-w-md"><div className="mb-8 flex justify-center"><Logo /></div><div className="text-center"><h1 className="text-3xl font-black">{isRegister ? 'Create your account' : 'Welcome back'}</h1><p className="mt-3 text-slate-400">Track, analyze, and dominate</p></div><form onSubmit={handleSubmit} className="mt-9 rounded-2xl border border-slate-800 bg-slate-950/70 p-7 shadow-2xl"><label className="block text-sm text-slate-400">Email</label><input className="mt-2 w-full rounded-lg border border-slate-800 bg-slate-900 px-4 py-3 text-white outline-none transition focus:border-cyan" placeholder="you@email.com" value={form.email} onChange={(event) => setForm({ ...form, email: event.target.value })} required />{isRegister && <><label className="mt-5 block text-sm text-slate-400">Username</label><input className="mt-2 w-full rounded-lg border border-slate-800 bg-slate-900 px-4 py-3 text-white outline-none transition focus:border-cyan" placeholder="ShadowStriker" value={form.username} onChange={(event) => setForm({ ...form, username: event.target.value })} required /></>}<label className="mt-5 block text-sm text-slate-400">Password</label><input className="mt-2 w-full rounded-lg border border-slate-800 bg-slate-900 px-4 py-3 text-white outline-none transition focus:border-cyan" placeholder="Min 8 characters" type="password" minLength={8} value={form.password} onChange={(event) => setForm({ ...form, password: event.target.value })} required />{status.error && <p className="mt-4 rounded-lg border border-red-500/30 bg-red-500/10 px-3 py-2 text-sm text-red-200">{status.error}</p>}{status.success && <p className="mt-4 rounded-lg border border-emerald-500/30 bg-emerald-500/10 px-3 py-2 text-sm text-emerald-200">{status.success}</p>}<Button className="mt-6 w-full" isLoading={status.loading}>{isRegister ? 'Create account' : 'Sign in'}</Button><div className="mt-5 grid grid-cols-2 gap-3"><Button type="button" variant="subtle" onClick={() => handleOAuth('google')}><Mail size={16} /> Google</Button><Button type="button" variant="subtle" onClick={() => handleOAuth('discord')}><Github size={16} /> Discord</Button></div></form><p className="mt-5 text-center text-slate-400">{isRegister ? 'Already have an account?' : 'Need an account?'} <Link className="font-bold text-cyan" to={isRegister ? '/login' : '/register'}>{isRegister ? 'Sign in' : 'Create one'}</Link></p></div></section>;
}
