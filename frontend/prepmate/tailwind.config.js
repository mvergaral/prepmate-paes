/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#4F46E5",
          light: "#6159E8",
          dark: "#3127E1",
        },
        secondary: {
          DEFAULT: "#14B8A6",
          light: "#17D4BF",
          dark: "#12A292",
        },
        accent: {
          DEFAULT: "#FACC15",
          light: "#FAD12C",
          dark: "#E9BC05",
        },
        background: {
          light: "#F8FAFC",
          dark: "#0F172A"
        },
        text: {
          light: "#1E293B",
          dark: "#F1F5F9",
          muted: "#64748B",
        },
      },
      fontFamily: {
        sans: ['Inter', 'Poppins', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

