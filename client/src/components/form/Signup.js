import React from "react";
import { useState } from "react";
import axios from "axios";


export const Signup = ({ onAuthenticate }) => {
    const [email, setEmail] = useState("");
    const [password1, setPasssword1] = useState("");
    const [password2, setPassword2] = useState("");

    async function registerUser() {
        const url = 'http://localhost:8003/api/user/sign-up/'
        await axios.post(
            url,
            email,
            password1,
            password2
        )
        .then((response) => {
            // Todo
            // Return access token from server when user signup
            const { user, accessToken } = response.data();
            onAuthenticate(user, accessToken)

        }, (error) => {
            console.log(error)
        });
    }


    const handleSubmit = async (e) =>  {
        e.preventDefault();
        registerUser();
    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset>
                <label>
                    email
                    <input 
                        type="email" 
                        value={ email } 
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
                    value={ password1 } 
                    onChange={(e) => setPasssword1(e.currentTarget.value)}
                    required 
                />
                </label>
            </fieldset>
            <fieldset>
                <label>
                    re-enter Password
                    <input 
                        type="password" 
                        value={ password2 } 
                        onChange={(e) => setPassword2(e.currentTarget.value)}
                        required />
                </label>
            </fieldset>
            <button type="submit">Sign Up</button>
        </form>
    );
};