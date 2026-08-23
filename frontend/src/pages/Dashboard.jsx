import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    try {
      setLoading(true);
      setError("");

      const response = await fetch(
        "http://127.0.0.1:8000/dashboard/stats"
      );

      if (!response.ok) {
        throw new Error("Failed to load dashboard");
      }

      const data = await response.json();
      setStats(data);
    } catch (err) {
      console.error(err);
      setError("Could not load dashboard data.");
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="dashboard-page">
        <h1>Dashboard</h1>
        <p>Loading dashboard...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="dashboard-page">
        <h1>Dashboard</h1>

        <div className="dashboard-error">
          {error}
        </div>
      </div>
    );
  }

  return (
    <div className="dashboard-page">

      {/* ================= HEADER ================= */}

      <div className="dashboard-header">
        <div>
          <div className="section-label">
            🚘 DEALERSHIP OVERVIEW
          </div>

          <h1>Dashboard</h1>

          <p>
            Overview of your dealership inventory.
          </p>
        </div>
      </div>


      {/* ================= STATISTICS ================= */}

      <div className="stats-grid">

        {/* Total Vehicles */}

        <div className="stat-card">
          <div className="stat-icon">
            🚘
          </div>

          <div>
            <p className="stat-label">
              TOTAL VEHICLES
            </p>

            <h2>
              {stats.total_cars}
            </h2>
          </div>
        </div>


        {/* Available Vehicles */}

        <div className="stat-card">
          <div className="stat-icon">
            ✓
          </div>

          <div>
            <p className="stat-label">
              AVAILABLE
            </p>

            <h2>
              {stats.available_cars}
            </h2>
          </div>
        </div>


        {/* Sold Vehicles */}

        <div className="stat-card">
          <div className="stat-icon">
            💰
          </div>

          <div>
            <p className="stat-label">
              SOLD
            </p>

            <h2>
              {stats.sold_cars}
            </h2>
          </div>
        </div>


        {/* Inventory Value */}

        <div className="stat-card">
          <div className="stat-icon">
            ₹
          </div>

          <div>
            <p className="stat-label">
              INVENTORY VALUE
            </p>

            <h2>
              ₹
              {Number(
                stats.total_inventory_value
              ).toLocaleString("en-IN")}
            </h2>
          </div>
        </div>

      </div>


      {/* ================= INVENTORY OVERVIEW ================= */}

      <div className="dashboard-section">

        {/* Heading + View Inventory */}

        <div className="dashboard-section-header">

          <h2>
            Inventory Overview
          </h2>

          <Link
            to="/inventory"
            className="view-inventory-btn"
          >
            🚘 View Inventory →
          </Link>

        </div>


        {/* Overview Card */}

        <div className="overview-card">

          {/* Total */}

          <div className="overview-row">
            <span>
              Total Vehicles
            </span>

            <strong>
              {stats.total_cars}
            </strong>
          </div>


          {/* Available */}

          <div className="overview-row">
            <span>
              Available Vehicles
            </span>

            <strong>
              {stats.available_cars}
            </strong>
          </div>


          {/* Sold */}

          <div className="overview-row">
            <span>
              Sold Vehicles
            </span>

            <strong>
              {stats.sold_cars}
            </strong>
          </div>


          {/* Inventory Value */}

          <div className="overview-row">
            <span>
              Total Inventory Value
            </span>

            <strong>
              ₹
              {Number(
                stats.total_inventory_value
              ).toLocaleString("en-IN")}
            </strong>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;