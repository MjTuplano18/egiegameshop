import React, { useState } from "react";
import "./SignIn.css";
import { Link, useNavigate } from "react-router-dom";

const SignIn = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSignIn = async () => {
    if (!username || !password) {
      setMessage("Please fill in both fields.");
      return;
    }

    setIsLoading(true);
    setMessage("");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/signin/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
        credentials: "include", // Include cookies if needed
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message); // Show success message
        // Redirect to home page after successful login
        setTimeout(() => {
          navigate("/");
        }, 1500);
      } else {
        setMessage(data.message || "Sign In failed!"); // Show error message
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("An error occurred. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <button className="back-button">
        <Link to="/">Back to Home Page</Link>
      </button>
      <div className="signin-container">
        <div className="form-container">
          <h2>Sign In</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <p className="terms">
            By signing in, you agree to our{" "}
            <a href="#">Terms of Use</a> and <a href="#">Privacy Policy</a>.
          </p>
          <button 
            className="signup-button" 
            onClick={handleSignIn}
            disabled={isLoading}
          >
            {isLoading ? "Signing In..." : "Sign In"}
          </button>
          {message && <p className={`message ${message.includes("successful") ? "success" : "error"}`}>{message}</p>}
          <p className="toggle-signin">
            Don't have an account?
            <Link to="/auth">
              Sign Up
            </Link>
          </p>
        </div>

        <div className="social-signup">
          <h3>Sign In with</h3>
          <button className="google-button">Google</button>
          <button className="facebook-button">Facebook</button>
        </div>
      </div>
    </>
  );
};

export default SignIn; 