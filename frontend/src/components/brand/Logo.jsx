import { Zap } from 'lucide-react';
export function Logo({ compact = false }) {
  return <div className="flex items-center gap-3"><div className="grid h-10 w-10 place-items-center rounded-xl bg-gradient-to-br from-cyan to-violet shadow-glow"><Zap size={20} fill="white" className="text-white" /></div>{!compact && <span className="font-display text-lg font-bold tracking-wide">GAMETRACKER</span>}</div>;
}
