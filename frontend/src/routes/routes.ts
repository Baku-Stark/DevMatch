// Centralização de todas as rotas da aplicação

export const ROUTES = {
  HOME: "/",
  ABOUT: "/pages/about",
  MENTORS: "/pages/mentors",
  MENTORSHIPS: "/pages/mentorships",
  SIGN_IN: "/pages/signIn",
  SIGN_UP: "/pages/singUp",

  // 🔹 Routes with dynamic parameters
  PROFILE: (id: string | number) => `/pages/profile_id=${id}`,

  // Example of nested routes
  SETTINGS: {
    ROOT: "/settings",
    ACCOUNT: "/settings/account",
    SECURITY: "/settings/security",
  },
} as const;

export type AppRoute = (typeof ROUTES)[keyof typeof ROUTES];