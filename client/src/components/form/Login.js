import React from "react";
import { useState } from "react"
import axios from "axios";
import useLoginFrom from "./useLoginForm";

const Login = ({ onAuthenticate }) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function loginUser() {
        const url = "http://localhost:8003/api/user/log-in/"
        await axios.post(
            url,
            email,
            password
        )
        .then((response) => {
            return response.data
        }, (error) => {
            console.log(error);
        });
    }

    // Call API
    const handleSubmit = async (e) => {
        e.preventDefault();
        const { user, accessToken } = loginUser();
        onAuthenticate(user, accessToken);
    }
 
    return (
        <form onSubmit={handleSubmit}>
            <fieldset>
                <label>
                    Email
                    <input 
                        type="email" 
                        value={email} 
                        onChange={(e) => setEmail(e.currentTarget.value)}
                        required 
                    />
                </label>
            </fieldset>
            <fieldset>
                <label>
                    Password
                    <input 
                        type="password" 
                        value={password}
                        onChange={(e) => setPassword(e.currentTarget.value)} 
                        required 
                    />
                </label>
            </fieldset>
            <button type="submit">LogIn</button>
        </form>
    );
}

export default Login;