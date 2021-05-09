import { useEffect, useState } from "react";
import { useHistory, useLocation } from "react-router";
import { useLoginSession } from "../../services/LoginSession";

import { Signup } from "./Signup";
import { Login } from "./Login";

export const AuthenticationForm = () => {
    const history = useHistory();
    const location = useLocation();

    const [hasAccount, setHasAccount] = useState(false);
    const { logIn, user } = useLoginSession();
    console.log("location", location.state)

    useEffect(() => {
        if (user) {
            history.replace(location.state?.from || '/')
        }
    }, []);

    const handleAuth = ({ user, token }) => {
        logIn(user, token)
        history.replace(location.state?.form || "/")
    }

    const toggleMethod = () => {
        setHasAccount((yes) => !yes);
    }

    return (
        <div>
            {hasAccount ? (
                <Signup onAuthenticate={handleAuth} />
            ) : (
                <Login onAuthenticate={handleAuth} />
            )}

            <button onClick={toggleMethod}>
                {hasAccount ? "Already have an Account?" : "Don't have an account yet?"}
            </button>
        </div>
    );
};
