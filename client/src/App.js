import React from "react";
import { Switch, Route } from "react-router-dom";

import HomePage from "./pages/homepage/homepage";
import LogInAndSignUpPage from "./pages/log-in-and-sign-up/log-in-and-sign-up";

function App() {
  return (
    <div>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/auth" component={LogInAndSignUpPage} />
      </Switch>
    </div>
  );
}

export default App;
