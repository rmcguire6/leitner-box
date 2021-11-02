import React, { useState } from "react";

const LogIn = () => {
  const [user, setUser] = useState({ name: "" });

  const handleSubmit = (event) => {
    event.preventDefault();
    // call to /auth/login
    console.log(`Current logged in user name: ${user.name}`);
  };
  const handleChange = (event) => {
    const { value, name } = event.target;
    setUser({ [name]: value });
  };
  return (
    <div>
      <h2>I already have an account</h2>
      <span>Log in with your name</span>
      <form className="container" onSubmit={handleSubmit}>
        <label>Your Name</label>
        <input
          name="name"
          type="text"
          value={user.name}
          onChange={handleChange}
          required
        />
        <input type="submit" value="Log In" />
      </form>
    </div>
  );
};
export default LogIn;
