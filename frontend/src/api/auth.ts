import type {LoginRequest, LoginResponse, RegisterRequest,} from "../types/auth.ts";
import api from "./client.ts";
export async function login(data: LoginRequest) {
    const response =await api.post<LoginResponse>("/auth/v1/login", data);
    return response.data;
}
export async function register(data: RegisterRequest) {
    const response =await api.post("/auth/v1/register", data);
    return response.data;
}

export async function getme(): Promise<void> {
    const response =await api.get<void>("/auth/v1/me");
    return response.data;
}
