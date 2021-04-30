import React, { useState } from "react";

const useSignUpForm = (callback) => {
    const [inputs, setInputs] = useState();

    const handleSubmit = (event) => {
        if (event) {
            // prevent default behavior such as refresh page
            event.preventDefault();
        }
        callback();
    }

    const handleInputChange = (event) => {
        event.persist();
        setInputs(inputs => ({...inputs, [event.trget.name]:
        event.target.value}));
    }
    return {
        handleSubmit,
        handleInputChange,
        inputs
    }
}

export default useSignUpForm;
