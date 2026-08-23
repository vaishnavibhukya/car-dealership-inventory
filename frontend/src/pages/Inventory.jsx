import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getCars,
  createCar,
  updateCar,
  deleteCar,
  purchaseCar,
  restockCar,
} from "../services/api";

import "./Inventory.css";

function Inventory() {
  const navigate = useNavigate();

  const [cars, setCars] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [showForm, setShowForm] = useState(false);
  const [editingCar, setEditingCar] = useState(null);

  const [formData, setFormData] = useState({
    make: "",
    model: "",
    year: "",
    price: "",
    mileage: "",
    color: "",
    quantity: 1,
  });

  // ============================================
  // LOAD CARS
  // ============================================

  useEffect(() => {
    loadCars();
  }, []);

  async function loadCars() {
    try {
      setLoading(true);
      setError("");

      const data = await getCars();

      setCars(data);
    } catch (err) {
      console.error(err);
      setError("Could not load vehicles.");
    } finally {
      setLoading(false);
    }
  }

  // ============================================
  // FORM INPUT
  // ============================================

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  // ============================================
  // ADD / UPDATE CAR
  // ============================================

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      const carData = {
        make: formData.make,
        model: formData.model,
        year: Number(formData.year),
        price: Number(formData.price),
        mileage: Number(formData.mileage),
        color: formData.color,
        quantity: Number(formData.quantity),
      };

      if (editingCar) {
        await updateCar(editingCar.id, carData);
      } else {
        await createCar(carData);
      }

      setShowForm(false);
      setEditingCar(null);

      setFormData({
        make: "",
        model: "",
        year: "",
        price: "",
        mileage: "",
        color: "",
        quantity: 1,
      });

      await loadCars();
    } catch (err) {
      console.error(err);
      setError(err.message || "Operation failed.");
    }
  }

  // ============================================
  // EDIT
  // ============================================

  function handleEdit(car) {
    setEditingCar(car);

    setFormData({
      make: car.make || "",
      model: car.model || "",
      year: car.year || "",
      price: car.price || "",
      mileage: car.mileage || "",
      color: car.color || "",
      quantity: car.quantity || 1,
    });

    setShowForm(true);

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  // ============================================
  // DELETE
  // ============================================

  async function handleDelete(carId) {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this vehicle?"
    );

    if (!confirmDelete) return;

    try {
      await deleteCar(carId);
      await loadCars();
    } catch (err) {
      console.error(err);
      setError(err.message || "Failed to delete vehicle.");
    }
  }

  // ============================================
  // PURCHASE
  // ============================================

  async function handlePurchase(carId) {
    try {
      await purchaseCar(carId);
      await loadCars();
    } catch (err) {
      console.error(err);
      setError(err.message || "Failed to purchase vehicle.");
    }
  }

  // ============================================
  // RESTOCK
  // ============================================

  async function handleRestock(carId) {
    try {
      await restockCar(carId);
      await loadCars();
    } catch (err) {
      console.error(err);
      setError(err.message || "Failed to restock vehicle.");
    }
  }

  // ============================================
  // FILTER SEARCH
  // ============================================

  const filteredCars = cars.filter((car) => {
    const searchText = search.toLowerCase();

    return (
      String(car.make || "")
        .toLowerCase()
        .includes(searchText) ||
      String(car.model || "")
        .toLowerCase()
        .includes(searchText) ||
      String(car.year || "")
        .includes(searchText) ||
      String(car.color || "")
        .toLowerCase()
        .includes(searchText)
    );
  });

  // ============================================
  // FORM
  // ============================================

  function renderForm() {
    return (
      <div className="inventory-form-card">
        <div className="form-header">
          <div>
            <p className="inventory-label">
              {editingCar ? "UPDATE VEHICLE" : "ADD VEHICLE"}
            </p>

            <h2>
              {editingCar ? "Edit Vehicle" : "Add New Vehicle"}
            </h2>
          </div>

          <button
            className="cancel-btn"
            onClick={() => {
              setShowForm(false);
              setEditingCar(null);
            }}
          >
            Cancel
          </button>
        </div>

        <form onSubmit={handleSubmit} className="vehicle-form">
          <div className="form-row">
            <div className="form-group">
              <label>Make</label>
              <input
                type="text"
                name="make"
                placeholder="Toyota"
                value={formData.make}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Model</label>
              <input
                type="text"
                name="model"
                placeholder="Corolla"
                value={formData.model}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Year</label>
              <input
                type="number"
                name="year"
                placeholder="2025"
                value={formData.year}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Price</label>
              <input
                type="number"
                name="price"
                placeholder="500000"
                value={formData.price}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Mileage</label>
              <input
                type="number"
                name="mileage"
                placeholder="15000"
                value={formData.mileage}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Color</label>
              <input
                type="text"
                name="color"
                placeholder="White"
                value={formData.color}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="form-group">
            <label>Quantity</label>
            <input
              type="number"
              name="quantity"
              min="1"
              value={formData.quantity}
              onChange={handleChange}
              required
            />
          </div>

          <button type="submit" className="submit-vehicle-btn">
            {editingCar ? "Update Vehicle" : "Add Vehicle"}
          </button>
        </form>
      </div>
    );
  }

  // ============================================
  // LOADING
  // ============================================

  if (loading) {
    return (
      <div className="inventory-page">
        <h1 className="inventory-title">Car Inventory</h1>
        <p className="inventory-subtitle">Loading vehicles...</p>
      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (
    <div className="inventory-page">

      {/* HEADER */}

      <div className="inventory-header">

        <div className="inventory-title-section">

          <div className="inventory-label">
            🚘 VEHICLE MANAGEMENT
          </div>

          <h1 className="inventory-title">
            Car Inventory
          </h1>

          <p className="inventory-subtitle">
            Manage and track your dealership vehicles.
          </p>

        </div>

        <button
          className="add-vehicle-btn"
          onClick={() => {
            setEditingCar(null);

            setFormData({
              make: "",
              model: "",
              year: "",
              price: "",
              mileage: "",
              color: "",
              quantity: 1,
            });

            setShowForm(true);
          }}
        >
          + Add Vehicle
        </button>

      </div>

      {/* ERROR */}

      {error && (
        <div className="inventory-error">
          {error}
        </div>
      )}

      {/* ADD / EDIT FORM */}

      {showForm && renderForm()}

      {/* SEARCH */}

      {!showForm && (
        <div className="inventory-search">

          <div className="search-box">

            <span className="search-icon">
              🔍
            </span>

            <input
              type="text"
              placeholder="Search vehicles..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />

          </div>

        </div>
      )}

      {/* COUNT */}

      <p className="inventory-count">
        {filteredCars.length}{" "}
        {filteredCars.length === 1
          ? "vehicle"
          : "vehicles"}{" "}
        in inventory
      </p>

      {/* VEHICLES */}

      {filteredCars.length === 0 ? (

        <div className="empty-inventory">

          <div className="empty-icon">
            🚘
          </div>

          <h2>No vehicles found</h2>

          <p>
            Try another search or add a new vehicle.
          </p>

        </div>

      ) : (

        <div className="vehicle-grid">

          {filteredCars.map((car) => (

            <div
              className="vehicle-card"
              key={car.id}
            >

              {/* IMAGE */}

              <div className="vehicle-image">
                <span>🚘</span>
              </div>

              {/* INFORMATION */}

              <div className="vehicle-info">

                <div className="vehicle-top">

                  <h2 className="vehicle-name">
                    {car.make} {car.model}
                  </h2>

                  <span
                    className={`vehicle-status ${
                      car.quantity > 0
                        ? "available"
                        : "sold"
                    }`}
                  >
                    {car.quantity > 0
                      ? "available"
                      : "sold"}
                  </span>

                </div>

                <p className="vehicle-details">
                  {car.year} • Automatic • Petrol
                </p>

                <p className="vehicle-price">
                  ₹{Number(car.price).toLocaleString("en-IN")}
                </p>

                {/* META */}

                <div className="vehicle-meta">

                  <div className="meta-item">
                    <p className="meta-label">
                      MILEAGE
                    </p>

                    <p className="meta-value">
                      {Number(
                        car.mileage
                      ).toLocaleString("en-IN")}{" "}
                      km
                    </p>
                  </div>

                  <div className="meta-item">
                    <p className="meta-label">
                      COLOR
                    </p>

                    <p className="meta-value">
                      {car.color}
                    </p>
                  </div>

                  <div className="meta-item">
                    <p className="meta-label">
                      QUANTITY
                    </p>

                    <p className="meta-value">
                      {car.quantity}
                    </p>
                  </div>

                </div>

                {/* BUTTONS */}

                <div className="vehicle-actions">

                  <button
                    className="edit-btn"
                    onClick={() =>
                      handleEdit(car)
                    }
                  >
                    ✏️ Edit
                  </button>

                  <button
                    className="delete-btn"
                    onClick={() =>
                      handleDelete(car.id)
                    }
                  >
                    🗑️ Delete
                  </button>

                </div>

                <div className="vehicle-actions">

                  {car.quantity > 0 ? (

                    <button
                      className="purchase-btn"
                      onClick={() =>
                        handlePurchase(car.id)
                      }
                    >
                      🛒 Purchase
                    </button>

                  ) : (

                    <button
                      className="restock-btn"
                      onClick={() =>
                        handleRestock(car.id)
                      }
                    >
                      🔄 Restock
                    </button>

                  )}

                </div>

              </div>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default Inventory;