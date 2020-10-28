import pkg from "./package";

module.exports = {
  server: {
    port: 4000, // default: 3000
    host: "0.0.0.0" // default: localhost
  },
  head: {
    title: "forfar_test",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: pkg.description }
    ],
    link: [
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css?family=PT+Serif:400,400i,700,700i&display=swap&subset=cyrillic,cyrillic-ext,latin-ext"
      },
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&display=swap&subset=cyrillic,cyrillic-ext,latin-ext,vietnamese"
      }
    ]
  },

  loading: { color: "#911451" },

  css: [
  ],

  plugins: [
  ],

  modules: ["@nuxtjs/svg", "@nuxtjs/axios", "@nuxtjs/proxy"],

  axios: {
    proxy: true
  },

  proxy: {
    "/api/": process.env["BE_URL"] || "http://localhost:8000/"
  },

  buildModules: [["@nuxtjs/moment"]],

  build: {
    extend(config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: "pre",
          test: /\.(js|vue)$/,
          loader: "eslint-loader",
          exclude: /(node_modules)/
        });
      }
    }
  }
};
