import { useState, useEffect } from "react";
import axios from "axios";

const useLoginForm = () => {
    const [inputs, setInputs] = useState({});

    async function loginUser() {
        const url = "http://localhost:8003/api/user/log-in/"
        console.log(inputs)
        await axios.post(
            url,
            inputs
        )
        .then((response) => {
            console.log(response)
        }, (error) => {
            console.log(error);
        });
    }

    useEffect(() => {
        loginUser();
    }, []) 

    const handleSubmit = (event) => {
        if (event) {
            event.preventDefault();
            loginUser();
        }
    }

    const handleInputChange = (event) => {
        event.persist();
        setInputs(inputs =>(
            {...inputs, 
            [event.target.name]:event.target.value
        }));
    }

    return {
        handleSubmit,
        handleInputChange,
        inputs
    }
}

export default useLoginForm;