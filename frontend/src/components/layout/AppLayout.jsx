import { Outlet } from 'react-router-dom';
export function AppLayout() {
  return <main className="min-h-screen bg-ink text-white antialiased"><Outlet /></main>;
}
