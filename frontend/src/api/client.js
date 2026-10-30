const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '';

export class ApiError extends Error {
  constructor(message, status, details = null) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.details = details;
  }
}

export async function fetchDetailedHealth() {
  const url = `${API_BASE_URL}/api/v1/health/detailed`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });

    if (!response.ok) {
      let errorDetails = null;
      try {
        errorDetails = await response.json();
      } catch {
        // Response wasn't json
      }
      throw new ApiError(
        `Failed to fetch system status (HTTP ${response.status})`,
        response.status,
        errorDetails
      );
    }

    return await response.json();
  } catch (err) {
    if (err instanceof ApiError) throw err;
    throw new ApiError(
      err.message || 'Network error connecting to AI Vision Trainer API',
      0
    );
  }
}
