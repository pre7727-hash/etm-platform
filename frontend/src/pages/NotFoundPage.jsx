import { Link } from 'react-router-dom';
import { Button } from '../components/ui/Button.jsx';
export function NotFoundPage() {
  return <section className="grid min-h-screen place-items-center px-6 text-center"><div><p className="font-display text-7xl font-black text-cyan">404</p><h1 className="mt-4 text-2xl font-black">Page not found</h1><p className="mt-3 text-slate-400">This route is not available yet.</p><Link to="/"><Button className="mt-8">Back to Home</Button></Link></div></section>;
}
