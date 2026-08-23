import { Link } from "react-router-dom";
import "../App.css";

function Home() {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#071321",
        color: "white",
      }}
    >
      {/* NAVBAR */}
      <nav
        style={{
          height: "90px",
          padding: "0 7%",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          borderBottom: "1px solid #263447",
        }}
      >
        {/* LOGO */}
        <div>
          <h2 style={{ fontSize: "28px", margin: 0 }}>
            🚘 AutoSphere
          </h2>

          <p
            style={{
              color: "#8298b2",
              fontSize: "12px",
              margin: "4px 0 0",
            }}
          >
            DEALERSHIP MANAGEMENT
          </p>
        </div>

        {/* NAVIGATION */}
        <div
          style={{
            display: "flex",
            gap: "30px",
            alignItems: "center",
          }}
        >
          <Link to="/">Home</Link>

          <Link to="/inventory">Inventory</Link>

          <Link to="/dashboard">Dashboard</Link>

          <Link to="/login">Login</Link>
        </div>
      </nav>

      {/* HERO SECTION */}
      <main
        style={{
          width: "85%",
          maxWidth: "1400px",
          margin: "0 auto",
          padding: "100px 0",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: "60px",
        }}
      >
        {/* LEFT SIDE */}
        <section style={{ maxWidth: "700px" }}>
          <div
            style={{
              display: "inline-block",
              padding: "10px 18px",
              border: "1px solid #2864e8",
              borderRadius: "30px",
              color: "#4c91ff",
              marginBottom: "30px",
            }}
          >
            ✦ SMART CAR INVENTORY MANAGEMENT
          </div>

          <h1
            style={{
              fontSize: "70px",
              lineHeight: "1",
              marginBottom: "30px",
            }}
          >
            Manage Your
            <br />

            <span style={{ color: "#347df4" }}>
              Dealership Smarter.
            </span>
          </h1>

          <p
            style={{
              color: "#9db3cf",
              fontSize: "20px",
              lineHeight: "1.7",
              marginBottom: "35px",
            }}
          >
            A modern inventory management system designed to help
            dealerships manage vehicles, track availability and handle
            purchases effortlessly.
          </p>

          {/* HERO BUTTONS */}
          <div
            style={{
              display: "flex",
              gap: "20px",
            }}
          >
            <Link
              to="/dashboard"
              style={{
                background: "#2864e8",
                padding: "18px 28px",
                borderRadius: "10px",
                fontWeight: "bold",
              }}
            >
              Dashboard →
            </Link>

            <Link
              to="/inventory"
              style={{
                border: "1px solid #344a66",
                padding: "18px 28px",
                borderRadius: "10px",
                fontWeight: "bold",
              }}
            >
              Explore Inventory
            </Link>
          </div>
        </section>

        {/* FEATURED VEHICLE */}
        <section
          style={{
            width: "500px",
            padding: "35px",
            borderRadius: "25px",
            background: "#12233a",
            border: "1px solid #263b55",
          }}
        >
          <p style={{ color: "#7187a3" }}>
            FEATURED VEHICLE
          </p>

          <div
            style={{
              height: "250px",
              marginTop: "20px",
              borderRadius: "18px",
              background: "#071525",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: "100px",
            }}
          >
            🚘
          </div>

          <h2
            style={{
              marginTop: "25px",
              fontSize: "28px",
            }}
          >
            Toyota Camry
          </h2>

          <p
            style={{
              color: "#7187a3",
              marginTop: "8px",
            }}
          >
            2024 • Automatic • Petrol
          </p>

          <h2
            style={{
              color: "#5ca0ff",
              marginTop: "20px",
            }}
          >
            ₹25,000
          </h2>
        </section>
      </main>
    </div>
  );
}

export default Home;