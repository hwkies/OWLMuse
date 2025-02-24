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
        "primary": "var(--primary)",
        "background": "var(--background)",
        "primary-dark": "var(--primary-dark)",
        "background-dark": "var(--background-dark)",
      },
    },
  },
  plugins: [],
} satisfies Config;
