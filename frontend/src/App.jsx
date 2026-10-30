import React from 'react';
import { SystemStatus } from './components/SystemStatus';
import { Layers, ShieldCheck, Terminal } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-surface-900 flex flex-col">
      {/* Navigation Bar */}
      <header className="border-b border-surface-700/80 bg-surface-800/60 backdrop-blur sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-lg bg-brand-600 flex items-center justify-center text-white shadow-lg shadow-brand-500/20">
              <Layers className="w-5 h-5" />
            </div>
            <div>
              <span className="font-bold text-lg text-white tracking-tight">AI Vision Trainer</span>
              <span className="ml-2 text-xs font-mono text-brand-400 bg-brand-500/10 px-2 py-0.5 rounded border border-brand-500/20">
                v1.0.0
              </span>
            </div>
          </div>

          <div className="flex items-center gap-4 text-xs text-slate-400">
            <span className="hidden sm:inline-flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              AGPL Gate Active
            </span>
            <span className="inline-flex items-center gap-1.5 font-mono bg-surface-700/50 px-2.5 py-1 rounded border border-surface-600">
              <Terminal className="w-3.5 h-3.5 text-slate-300" />
              API /api/v1
            </span>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <SystemStatus />
      </main>

      {/* Footer */}
      <footer className="border-t border-surface-800 py-6 text-center text-xs text-slate-500">
        AI Vision Trainer &bull; Self-hosted Supervised YOLO Object Detection Platform
      </footer>
    </div>
  );
}
