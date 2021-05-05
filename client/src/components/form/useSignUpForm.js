import React, { useEffect, useState } from "react";
import axios from "axios";

const useSignUpForm = () => {
    // initialize state
    const [inputs, setInputs] = useState({});

    async function registerUser() {
        const url = 'http://localhost:8003/api/user/sign-up/'
        await axios.post(
            url,
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
