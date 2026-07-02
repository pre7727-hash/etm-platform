export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        display: ['Orbitron', 'Inter', 'ui-sans-serif', 'system-ui']
      },
      colors: {
        ink: '#05070d',
        panel: '#0c1018',
        panelSoft: '#111722',
        line: '#222a37',
        cyan: '#16d9ff',
        violet: '#7657ff',
        electric: '#2689ff'
      },
      boxShadow: { glow: '0 0 40px rgba(22, 217, 255, 0.2)' }
    }
  },
  plugins: []
};
