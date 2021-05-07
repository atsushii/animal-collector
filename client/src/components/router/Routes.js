import React from "react";
import Signup from "../form/Signup";
import Login from "../form/Login";
import DashBoard from "../mainpage/DashBoard"

const routes = {
    "/signup": () => <Signup />,
    "/login": () => <Login />,
    "/dashboard": () => <DashBoard />
};


export default routes;
