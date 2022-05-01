const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        Inter: ["Inter", "sans-serif"],
      },
    },
    colors: {
      'naranja-usach': '#F38A24',
      'azul-usach': '#004883',
      'azulHoverUsach': '#0259A0',
      'gris-usach': '#C4C4C4',
      'white': colors.white,
      'gray': colors.gray,
      'indigo': colors.indigo,
      'red': colors.red,
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
