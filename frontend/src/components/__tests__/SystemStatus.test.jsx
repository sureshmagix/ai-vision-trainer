import React from 'react';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { SystemStatus } from '../SystemStatus';
import * as client from '../../api/client';

describe('SystemStatus Component', () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  const mockHealthSuccess = {
    status: 'healthy',
    app_name: 'AI Vision Trainer',
    version: '1.0.0',
    environment: 'development',
    timestamp: '2026-10-30T18:00:00Z',
    uptime_seconds: 124.5,
    database: {
      status: 'connected',
      latency_ms: 1.45,
      engine: 'postgresql',
    },
    redis: {
      status: 'connected',
      latency_ms: 0.85,
    },
    hardware: {
      cpu_percent: 14.2,
      memory_percent: 42.1,
      memory_used_gb: 6.8,
      memory_total_gb: 16.0,
      disk_free_gb: 120.5,
      accelerator: 'cpu',
      accelerator_available: false,
    },
  };

  it('renders system identity and fetches live diagnostics', async () => {
    vi.spyOn(client, 'fetchDetailedHealth').mockResolvedValueOnce(mockHealthSuccess);

    render(<SystemStatus />);

    // Brand title present
    expect(screen.getByText('AI Vision Trainer')).toBeInTheDocument();

    // Await async API population
    await waitFor(() => {
      expect(screen.getByText('Healthy')).toBeInTheDocument();
      expect(screen.getByText('14.2%')).toBeInTheDocument();
      expect(screen.getByText(/postgresql/i)).toBeInTheDocument();
      expect(screen.getByText(/1.45/i)).toBeInTheDocument();
    });
  });

  it('handles backend connection failure gracefully with accessible alert', async () => {
    vi.spyOn(client, 'fetchDetailedHealth').mockRejectedValueOnce(
      new Error('Connection refused to backend API')
    );

    render(<SystemStatus />);

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeInTheDocument();
      expect(screen.getByText(/Connection refused to backend API/i)).toBeInTheDocument();
    });
  });
});
