const API_URL = "http://127.0.0.1:8000";

// ============================================================
// REGISTER
// ============================================================

export async function registerUser(username, password) {
  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Registration failed");
  }

  return response.json();
}


// ============================================================
// LOGIN
// ============================================================

export async function loginUser(username, password) {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Login failed");
  }

  return response.json();
}


// ============================================================
// GET ALL CARS
// ============================================================

export async function getCars() {
  const response = await fetch(`${API_URL}/cars/`);

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to fetch cars");
  }

  return response.json();
}


// ============================================================
// GET SINGLE CAR
// ============================================================

export async function getCar(carId) {
  const response = await fetch(`${API_URL}/cars/${carId}`);

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to fetch car");
  }

  return response.json();
}


// ============================================================
// CREATE CAR
// ============================================================

export async function createCar(carData) {
  const response = await fetch(`${API_URL}/cars/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(carData),
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to create car");
  }

  return response.json();
}


// ============================================================
// UPDATE CAR
// ============================================================

export async function updateCar(carId, carData) {
  const response = await fetch(`${API_URL}/cars/${carId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(carData),
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to update car");
  }

  return response.json();
}


// ============================================================
// DELETE CAR
// ============================================================

export async function deleteCar(carId) {
  const response = await fetch(`${API_URL}/cars/${carId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to delete car");
  }

  return response.json();
}


// ============================================================
// PURCHASE CAR
// ============================================================

export async function purchaseCar(carId) {
  const response = await fetch(
    `${API_URL}/cars/${carId}/purchase`,
    {
      method: "POST",
    }
  );

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to purchase car");
  }

  return response.json();
}


// ============================================================
// RESTOCK CAR
// ============================================================

export async function restockCar(carId) {
  const response = await fetch(
    `${API_URL}/cars/${carId}/restock`,
    {
      method: "POST",
    }
  );

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Failed to restock car");
  }

  return response.json();
}


// ============================================================
// DASHBOARD STATS
// ============================================================

export async function getDashboardStats() {
  const response = await fetch(
    `${API_URL}/dashboard/stats`
  );

  if (!response.ok) {
    const message = await response.text();
    throw new Error(
      message || "Failed to fetch dashboard statistics"
    );
  }

  return response.json();
}