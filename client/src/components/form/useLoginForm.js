import { useState, useEffect } from "react";
import axios from "axios";


const useLoginForm = () => {
    const [inputs, setInputs] = useState({});

    async function loginUser() {
        const url = "http://localhost:8003/api/user/log-in/"
        await axios.post(
            url,
            inputs
        )
        .then((response) => {
            if (response.data.access) {
                localStorage.setItem("user", JSON.stringify(response.data))
            }
            console.log("response")
            // todo
            // redirect tp dashboard after success login
            // share user data beteen login and dhashboard
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