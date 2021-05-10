import { createContext, useContext, useState} from "react";

const LoginSessionContext = createContext();

export const useLoginSession = () => {
    return useContext(LoginSessionContext);
}

export const LoginSessionProvider = ({ children }) => {
    const [accessToken, setAccessToken] = useState();
    const [user, setUser] = useState();

    const logIn = (user, accessToken) => {
        setAccessToken(accessToken);
        setUser(user)
    };

    const logOut = () => {
        setAccessToken(undefined);
        setUser(undefined);
    }

    const provider = {
        accessToken,
        user, 
        logIn,
        logOut
    };

    return (
        <LoginSessionContext.Provider value={provider}>
            {children}
        </LoginSessionContext.Provider>
    );
};