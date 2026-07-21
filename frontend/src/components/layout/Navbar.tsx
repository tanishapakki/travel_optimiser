import { Link, useNavigate } from "react-router-dom";
import { useAuthStore } from "../../store/authStore";

export default function Navbar() {
    const navigate = useNavigate();

    const user = useAuthStore((s) => s.user);
    const logout = useAuthStore((s) => s.logout);

    const handleLogout = () => {
        logout();
        navigate("/login");
    };

    return (
        <header className="border-b bg-white">
            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
                <Link
                    to="/dashboard"
                    className="text-xl font-bold"
                >
                    Travel Optimizer
                </Link>

                <div className="flex items-center gap-4">
                    <span className="text-sm text-gray-600">
                        {user?.name ?? user?.email}
                    </span>

                    <button
                        onClick={handleLogout}
                        className="rounded bg-red-500 px-4 py-2 text-white hover:bg-red-600"
                    >
                        Logout
                    </button>
                </div>
            </div>
        </header>
    );
}