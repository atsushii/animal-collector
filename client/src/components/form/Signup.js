import React from "react";

const Signup = () => {
    return (
        <form>
            <div>
                <label>email</label>
                <input type="email" name="email" required />
            </div>
            <div>
                <label>Password</label>
                <input type="password" name="password1" required />
            </div>
            <div>
                <label>re-enter Password</label>
                <input type="password" name="password2" required />
            </div>
            <button type="submit">Sign Up</button>
        </form>
    );
}

export default Signup;