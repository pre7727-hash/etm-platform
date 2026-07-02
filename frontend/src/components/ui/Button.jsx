import { Loader2 } from 'lucide-react';
const variants = {
  primary: 'bg-gradient-to-r from-violet to-cyan text-white shadow-glow hover:brightness-110',
  ghost: 'border border-white/10 bg-white/5 text-white hover:bg-white/10',
  subtle: 'border border-line bg-panelSoft text-white hover:border-cyan/40'
};
export function Button({ children, variant = 'primary', isLoading = false, className = '', ...props }) {
  return <button className={'inline-flex min-h-11 items-center justify-center gap-2 rounded-lg px-5 text-sm font-bold transition disabled:cursor-not-allowed disabled:opacity-60 ' + variants[variant] + ' ' + className} disabled={isLoading || props.disabled} {...props}>{isLoading && <Loader2 size={16} className="animate-spin" />}{children}</button>;
}
