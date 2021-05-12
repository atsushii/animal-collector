import React from "react";
import { Redirect, Route, Switch } from "react-router";
import { BrowserRouter } from "react-router-dom";

import { LoginSessionProvider, useLoginSession } from "../../services/LoginSession"
import { AuthenticationPage } from "../form/AuthenticationPage"
import { DashBoard } from "../mainpage/DashBoard"


export const Routes = () => {
    return (        
            <LoginSessionProvider>
                <BrowserRouter>
                    <Switch>
                    <Route path="/login" exact>
                            <AuthenticationPage />
                        </Route>
                        <ProtectRoute path="/" exact>
                            <DashBoard />
                        </ProtectRoute>
                        <Route path="*">
                            <NotFoundPage />
                        </Route>
                    </Switch>
                </BrowserRouter>
            </LoginSessionProvider>
    );
};

const ProtectRoute = ({ children, ...props }) => {
    const { user } = useLoginSession();

    return (
        <Route
            {...props}
            render={({ location }) => {
                if (user) {
                    return children;
                }

                return ( 
                    <Redirect to={{ pathname: "/login", state: { from: location } }} />
                );
            }}
        />
    );
};

const NotFoundPage = () => {
    return (
        <>
            <h1>404: Page Not Found</h1>
        </>
    )
}