import React from "react";
import Signup from "../form/Signup";
import Login from "../form/Login";

const routes = {
    "/signup": () => <Signup />,
    "/login": () => <Login />
};

export default routes;
