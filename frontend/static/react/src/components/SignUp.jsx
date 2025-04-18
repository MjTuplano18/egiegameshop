import React, { useState } from "react";
import "./SignUp.css"; // Ensure this file exists and styles your component
import { Link, useNavigate } from "react-router-dom";

const SignUp = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSignUp = async () => {
    // Validate input fields
    if (!username || !email || !password) {
      setMessage("Please fill in all fields.");
      return;
    }

    // Basic validation
    if (password.length < 6) {
      setMessage("Password must be at least 6 characters long.");
      return;
    }

    if (!email.includes('@')) {
      setMessage("Please enter a valid email address.");
      return;
    }

    setIsLoading(true);
    setMessage("");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/signup/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, email, password }),
        credentials: "include", // Include cookies if needed
      });
    
      const data = await response.json();
      
      if (response.ok) {
        setMessage(data.message); // Show success message
        // Redirect to sign in page after successful signup
        setTimeout(() => {
          navigate("/signin");
        }, 2000);
      } else {
        setMessage(data.message || "Sign Up failed!"); // Show error message
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("An error occurred. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="signup-container">
      <div className="form-container">
        <h2>Sign Up</h2>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <a href="#" className="forgot-password">
          Forgot your Password?
        </a>
        <button 
          className="signup-button" 
          onClick={handleSignUp}
          disabled={isLoading}
        >
          {isLoading ? "Signing Up..." : "Sign Up"}
        </button>
        {message && <p className={`message ${message.includes("successfully") ? "success" : "error"}`}>{message}</p>}
        <p className="toggle-signin">
          Already have an account?{" "}
          <Link to="/signin">
            Sign In here
          </Link>
        </p>
      </div>

      <div className="social-signup">
        <h3>Sign Up with</h3>
        <button className="google-button">Google</button>
        <button className="facebook-button">Facebook</button>
      </div>
    </div>
  );
};

export default SignUp; 