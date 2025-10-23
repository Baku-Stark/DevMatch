import { useAuth, type IUserRegister } from "../../context/AuthContext";

/**
 * Function that makes the POST to the backend (FastAPI)
 * @param request IUserRegister
 * @returns response API data
 */
export async function SignUpService(request: IUserRegister){
    const { signup } = useAuth();
    

    // Basic validation before the API call
    if (!request.name || !request.email || !request.password || !request.confirmPassword) {
        throw new Error("All fields are required.");
    }

    if (request.password !== request.confirmPassword) {
        throw new Error("Passwords do not match!");
    }

    await signup({
        name: request?.name as string,
        email: request?.email as string,
        password: request?.password as string,
    });

    try {
        // const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/signup`, {
        //         method: "POST",
        //         headers: {
        //             "Content-Type": "application/json",
        //     },
        //     body: JSON.stringify({
        //         name: request.name,
        //         email: request.email,
        //         password: request.password,
        //     }),
        // });

        // if (!response.ok) {
        //     const errorData = await response.json();
        //     throw new Error(errorData.message || "Failed to create account.");
        // }

        //return response;
    } catch (error: any) {
        console.error("SignUpService error:", error.message);
        throw error;
    }
}
