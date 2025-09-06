// Centralização de todas as rotas da aplicação

export const ROUTES = {
  HOME: "/",
  ABOUT: "/pages/about",
  DASHBOARD: "/pages/dashboard",
  MENTORS: "/pages/mentors",
  MENTORSHIPS: "/pages/mentorships",

  // 🔹 Routes with dynamic parameters
  PROFILE: (id: string | number) => `/pages/profile_id=${id}`,
  EDIT_PROFILE: (id: string | number) => `/pages/profile/edit/${id}`,
  CHAT: (chatId: string) => `/chat/${chatId}`,

  // Example of nested routes
  SETTINGS: {
    ROOT: "/settings",
    ACCOUNT: "/settings/account",
    SECURITY: "/settings/security",
  },
} as const;

export type AppRoute = (typeof ROUTES)[keyof typeof ROUTES];