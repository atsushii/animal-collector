import React from "react";
import useSignUpForm from "./CustomHooks";

const Signup = () => {
    const {inputs, handleInputChange, handleSubmit} = useSignUpForm();

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>email</label>
                <input type="email" name="email" onChange={handleInputChange}
                value={inputs.email} required />
            </div>
            <div>
                <label>Password</label>
                <input type="password" name="password1" onChange={handleInputChange}
                value={inputs.password1} required />
            </div>
            <div>
                <label>re-enter Password</label>
                <input type="password" name="password2" onChange={handleInputChange}
                value={inputs.password2} required />
            </div>
            <button type="submit">Sign Up</button>
        </form>
    );
}

export default Signup;