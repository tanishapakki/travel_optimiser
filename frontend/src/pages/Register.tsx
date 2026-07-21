import {useNavigate} from "react-router-dom";
import {type FormEvent, useState} from "react";
import {register} from "../api/auth.ts";

export default function Register () {
    const navigate = useNavigate();

    const [name, setName] = useState("");

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    async function handleSubmit(e: FormEvent) {
        e.preventDefault();

        setError("");

        try {
            await register({
                name,
                email,
                password,
            });

            navigate("/login");
        } catch (err: any) {
            setError(
                err.response?.data?.detail ??
                "Registration failed"
            );
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            ...
        </form>
    );
};