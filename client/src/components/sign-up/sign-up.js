import { useState } from 'react';
const SignUp = () => {
  const [name, setName] = useState('');
  const [cardsPerDay, setCardsPerDay] = useState(1);
  const handleSubmit = (e) => {
    e.preventDefault();
    // call to /auth_register
    console.log(`New user: ${name}`);
  };

  return (
    <>
      <h2>I do not have an account</h2>
      <span>Sign up with your name</span>
      <form className="container" onSubmit={handleSubmit}>
        <label>Your Name</label>
        <input
          name="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <label>Number of New Card(s) Per Day</label>
        <input
          name="cardsPerDay"
          type="integer"
          value={cardsPerDay}
          onChange={(e) => setCardsPerDay(e.target.value)}
          required
        />
        <input type="submit" value="Sign Up" />
      </form>
    </>
  );
};
export default SignUp;
