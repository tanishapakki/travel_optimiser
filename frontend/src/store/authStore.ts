
import {create} from "zustand";
import {persist} from "zustand/middleware";
import * as authApi from "../api/auth"

interface AuthState {
    user: any | null;
    token: string | null;
    login:(
        email: string,
        password: string,
    ) => Promise<void>;

    logout: () =>void;

    fetchUsers: () => Promise<void>;
}

export const useAuthStore = create<AuthState>()(
    persist(
        (set,get) =>({
                user: null,
                token: null,
                async login(email, password) {
                    const data = await authApi.login({ email, password });

                    set({
                        token: data.access_token,
                    });

                    const me = await authApi.getme();

                    set({
                        user: me,
                    });
                },

                async fetchUsers(){
                    if (!get().token) return;

                    const me = await authApi.getme();

                    set({
                        user: me,
                    })
                },

                logout(){
                    set({user: null,
                    token: null});
                },
            }),
        {
            name: "auth-storage",
        }
    )
)