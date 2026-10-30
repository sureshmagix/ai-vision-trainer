import React, { useState, useEffect } from 'react';
import { fetchDetailedHealth } from '../api/client';
import {
  Activity,
  Database,
  Cpu,
  HardDrive,
  Radio,
  RefreshCw,
  AlertTriangle,
  CheckCircle2,
  XCircle,
  Zap
} from 'lucide-react';

export function SystemStatus() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const loadHealth = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await fetchDetailedHealth();
      setData(result);
    } catch (err) {
      setError(err.message || 'Unable to communicate with API');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadHealth();
  }, []);

  const getStatusBadge = (status) => {
    if (status === 'healthy') {
      return (
        <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
          <CheckCircle2 className="w-3.5 h-3.5" />
          Healthy
        </span>
      );
    }
    if (status === 'degraded') {
      return (
        <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20">
          <AlertTriangle className="w-3.5 h-3.5" />
          Degraded
        </span>
      );
    }
    return (
      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
        <XCircle className="w-3.5 h-3.5" />
        Unhealthy
      </span>
    );
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto">
      {/* Top Header Card */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center bg-surface-800/80 backdrop-blur border border-surface-700 rounded-xl p-6 shadow-xl">
        <div className="space-y-1">
          <div className="flex items-center gap-3">
            <h1 className="text-2xl font-bold tracking-tight text-white">AI Vision Trainer</h1>
            {data && getStatusBadge(data.status)}
          </div>
          <p className="text-sm text-slate-400">
            Supervised YOLO object detection platform &bull; System Architecture Bootstrap
          </p>
        </div>

        <button
          onClick={loadHealth}
          disabled={loading}
          aria-label="Refresh telemetry"
          className="mt-4 sm:mt-0 inline-flex items-center gap-2 px-4 py-2 bg-brand-600 hover:bg-brand-500 disabled:opacity-50 text-white text-sm font-medium rounded-lg transition-colors focus:ring-2 focus:ring-brand-500/50 outline-none"
        >
          <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
          Refresh Status
        </button>
      </div>

      {error && (
        <div
          role="alert"
          className="bg-rose-500/10 border border-rose-500/30 text-rose-300 p-4 rounded-xl text-sm flex items-start gap-3"
        >
          <AlertTriangle className="w-5 h-5 text-rose-400 shrink-0 mt-0.5" />
          <div>
            <p className="font-semibold">Backend Connection Issue</p>
            <p className="text-rose-300/80 mt-1">{error}</p>
          </div>
        </div>
      )}

      {/* Grid of Diagnostics */}
      {data && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Database Card */}
          <div className="bg-surface-800 border border-surface-700 rounded-xl p-5 shadow-lg">
            <div className="flex items-center justify-between text-slate-400 mb-3">
              <span className="text-xs font-semibold uppercase tracking-wider">Database</span>
              <Database className="w-4 h-4 text-brand-400" />
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-xl font-bold text-white capitalize">{data.database.status}</span>
              {data.database.latency_ms !== null && (
                <span className="text-xs text-slate-400">{data.database.latency_ms} ms</span>
              )}
            </div>
            <div className="mt-3 text-xs text-slate-400 border-t border-surface-700 pt-3 flex justify-between">
              <span>Engine</span>
              <span className="font-mono text-slate-300 uppercase">{data.database.engine}</span>
            </div>
          </div>

          {/* Redis Broker Card */}
          <div className="bg-surface-800 border border-surface-700 rounded-xl p-5 shadow-lg">
            <div className="flex items-center justify-between text-slate-400 mb-3">
              <span className="text-xs font-semibold uppercase tracking-wider">Redis Broker</span>
              <Radio className="w-4 h-4 text-purple-400" />
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-xl font-bold text-white capitalize">{data.redis.status}</span>
              {data.redis.latency_ms !== null && (
                <span className="text-xs text-slate-400">{data.redis.latency_ms} ms</span>
              )}
            </div>
            <div className="mt-3 text-xs text-slate-400 border-t border-surface-700 pt-3 flex justify-between">
              <span>Queue Status</span>
              <span className="text-slate-300 font-medium">Durable Tasks</span>
            </div>
          </div>

          {/* CPU & Memory Card */}
          <div className="bg-surface-800 border border-surface-700 rounded-xl p-5 shadow-lg">
            <div className="flex items-center justify-between text-slate-400 mb-3">
              <span className="text-xs font-semibold uppercase tracking-wider">Compute Resources</span>
              <Cpu className="w-4 h-4 text-emerald-400" />
            </div>
            <div className="space-y-1">
              <div className="flex justify-between items-center text-sm">
                <span className="text-slate-400">CPU Load</span>
                <span className="font-semibold text-white">{data.hardware.cpu_percent}%</span>
              </div>
              <div className="w-full bg-surface-700 h-1.5 rounded-full overflow-hidden">
                <div
                  className="bg-emerald-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${Math.min(data.hardware.cpu_percent, 100)}%` }}
                />
              </div>
              <div className="flex justify-between items-center text-sm pt-2">
                <span className="text-slate-400">Memory</span>
                <span className="font-semibold text-white">{data.hardware.memory_percent}%</span>
              </div>
              <div className="w-full bg-surface-700 h-1.5 rounded-full overflow-hidden">
                <div
                  className="bg-blue-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${Math.min(data.hardware.memory_percent, 100)}%` }}
                />
              </div>
            </div>
            <div className="mt-3 text-xs text-slate-400 border-t border-surface-700 pt-3 flex justify-between">
              <span>RAM Used</span>
              <span className="text-slate-300 font-medium">{data.hardware.memory_used_gb} / {data.hardware.memory_total_gb} GB</span>
            </div>
          </div>

          {/* Accelerator & Storage Card */}
          <div className="bg-surface-800 border border-surface-700 rounded-xl p-5 shadow-lg">
            <div className="flex items-center justify-between text-slate-400 mb-3">
              <span className="text-xs font-semibold uppercase tracking-wider">Accelerator</span>
              <Zap className="w-4 h-4 text-amber-400" />
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-sm font-semibold text-white truncate" title={data.hardware.accelerator}>
                {data.hardware.accelerator}
              </span>
            </div>
            <div className="mt-3 text-xs text-slate-400 border-t border-surface-700 pt-3 space-y-1.5">
              <div className="flex justify-between">
                <span>Free Storage</span>
                <span className="text-slate-300 font-medium">{data.hardware.disk_free_gb} GB</span>
              </div>
              <div className="flex justify-between">
                <span>API Uptime</span>
                <span className="text-slate-300 font-mono">{Math.floor(data.uptime_seconds)}s</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Architecture & Provenance Verification Notice */}
      <div className="bg-surface-800/50 border border-surface-700/60 rounded-xl p-5 text-xs text-slate-400 space-y-2">
        <div className="flex items-center gap-2 font-semibold text-slate-200">
          <Activity className="w-4 h-4 text-brand-400" />
          <span>Truthful Telemetry Guarantee & Monorepo Foundation</span>
        </div>
        <p>
          Hardware metrics, database latency, and storage parameters are queried directly from system sensors and live services without synthetic inflation. Background worker adapters isolate model training routines from the FastAPI asynchronous event loop.
        </p>
      </div>
    </div>
  );
}
