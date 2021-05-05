import React from "react";
import useLoginFrom from "./useLoginForm";

const Login = () => {
    const {inputs, handleSubmit, handleInputChange} = useLoginFrom();
    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email</label>
                <input type="email" name="email" onChange={handleInputChange}
                value={inputs.email} required />
            </div>
            <div>
                <label>Password</label>
                <input type="password" name="password" onChange={handleInputChange} 
                value={inputs.password}  required />
            </div>
            <button type="submit">LogIn</button>
        </form>
    );
}

export default Login;