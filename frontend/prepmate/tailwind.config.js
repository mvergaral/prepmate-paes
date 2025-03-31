/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: "#4F46E5",
        secondary: "#14B8A6",
        accent: "#FACC15",
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

