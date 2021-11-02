import { Link } from "react-router-dom";

const Header = () => {
  return (
    <div className="main-nav">
      <Link className="nav-link" to="/">
        HOME
      </Link>
      <Link className="nav-link" to="/auth/register">
        LOGIN
      </Link>
      <Link className="nav-link" to="/auth/login">
        SIGNUP
      </Link>
    </div>
  );
};
export default Header;
