import React from "react";

const Login = () => {
    return (
        <form>
            <div>
                <label>Email</label>
                <input type="email" name="email" required />
            </div>
            <div>
                <label>Password</label>
                <input type="password" name="password" required />
            </div>
            <button type="submit">LogIn</button>
        </form>
    );
}

export default Login;