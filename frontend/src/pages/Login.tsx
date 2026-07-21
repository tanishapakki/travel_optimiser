import {useNavigate} from "react-router-dom";
import {useAuthStore} from "../store/authStore.ts";
import {type FormEvent, useState} from "react";

export default function LoginPage () {
    const navigate = useNavigate();

    const login = useAuthStore((s) => s.login);

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    async function handleSubmit(e: FormEvent) {
        e.preventDefault();

        setError("");

        try {
            await login(email, password);

            navigate("/dashboard");
        } catch (err: any) {
            setError(
                err.response?.data?.detail ??
                "Login failed"
            );
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                value={email}
                onChange={(e) =>
                    setEmail(e.target.value)
                }
            />

            <input
                type="password"
                value={password}
                onChange={(e) =>
                    setPassword(e.target.value)
                }
            />

            {error && <p>{error}</p>}

            <button>
                Login
            </button>
        </form>
    );
};