import React from "react";
import { useState } from "react"
import axios from "axios";

export const Login = ({ onAuthenticate }) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function loginUser() {
        const url = "http://localhost:8003/api/user/log-in/"
        await axios.post(
            url,
            {
                email,
                password
            }
        )
        .then((response) => {
            const {user, accessToken } = response.data
            console.log("here");
            onAuthenticate(user, accessToken);
        }, (error) => {
            console.log(error);
        });
    }

    // Call API
    const handleSubmit = (e) => {
        e.preventDefault();
        loginUser();
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