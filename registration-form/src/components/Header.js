import React from "react";
import { Link } from "react-router-dom";
import "./Header.css"; // Styling

const Header = () => {
  return (
    <nav className="header">
      <h2>Job Finder</h2>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/jobs">Jobs</Link>
        <Link to="/colleges">Colleges</Link>
        <Link to="/data">View Data</Link>
      </div>
    </nav>
  );
};

export default Header;
