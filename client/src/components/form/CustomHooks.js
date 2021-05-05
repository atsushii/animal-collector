import React, { useEffect, useState } from "react";
import axios from "axios";

const useSignUpForm = (callback) => {
    // initialize state
    const [inputs, setInputs] = useState({});

    async function registerUser() {
        console.log(inputs)
        await axios.post(
            'http://localhost:8003/api/user/sign-up/',
            inputs
        )
        .then((response) => {
            console.log(response);
        }, (error) => {
            console.log(error)
        });
    }

    useEffect(() => {
        registerUser();
    }, [])

    const handleSubmit = (event) => {
        if (event) {
            // prevent default behavior such as refresh page
            event.preventDefault();
            registerUser()
        }
    }

    const handleInputChange = (event) => {
        event.persist();
        setInputs(inputs => ({...inputs, [event.target.name]:
        event.target.value}));
    }
    return {
        handleSubmit,
        handleInputChange,
        inputs
    }
}

export default useSignUpForm;
