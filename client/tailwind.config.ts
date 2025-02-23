import type { Config } from "tailwindcss";

export default {
  darkMode: "selector",
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        "background": "var(--background)",
        "foreground": "var(--foreground)",
        "primary": "var(--primary)",
        "secondary": "var(--secondary)",
        "accent": "var(--accent)",
        "background-dark": "var(--background-dark)",
        "foreground-dark": "var(--foreground-dark)",
        "primary-dark": "var(--primary-dark)",
        "secondary-dark": "var(--secondary-dark)",
        "accent-dark": "var(--accent-dark)",
      },
    },
  },
  plugins: [],
} satisfies Config;
